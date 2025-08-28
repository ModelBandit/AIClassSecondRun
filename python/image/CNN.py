import os
import argparse
from typing import List, Tuple, Set
import numpy as np
import imageio
from ultralytics import YOLO
from PIL import Image, ImageDraw, ImageFont

def ensure_font():
    for p in [
        r"C:\Users\user\AppData\Local\Microsoft\Windows\Fonts\D2Coding-Ver1.3.2-20180524-all.ttc"
        ]:
        if os.path.isfile(p):
            try:
                return ImageFont.truetype(p,16)
            except Exception:
                pass
        return ImageFont.load_default()

# 모델경로
def resolve_model_source(model_arg:str)->str:
    if os.path.isfile(model_arg):
        return model_arg
    return model_arg

# 분류할 클래스 이름?
def get_class_names(model) -> List[str]:
    names = model.names
    if isinstance(names, dict):
        return [names[i] for i in sorted(names.keys())]
    return list(names)

# IoU 계산
def iou_xyxy(a:np.ndarray, b:np.ndarray) -> float:
    x1 = max(a[0], b[0])
    y1 = max(a[1], b[1])
    x2 = max(a[2], b[2])
    y2 = max(a[3], b[3])
    iw = max(0.0, x2-x1)
    ih = max(0.0, y2-y1)

    inter = iw * ih
    if inter <= 0:
        return 0.0
    
    area_a = (a[2]-a[0]) * (a[3]-a[1])
    area_b = (b[2]-b[0]) * (b[3]-b[1])
    union = area_a + area_b - inter

    if union <= 0:
        return 0.0
    return inter / union

class Track:
    __slots__ = ("tid", "bbox", "hits", "missed")
    def __init__(self, tid:int, bbox:np.ndarray):
        self.tid = tid
        self.bbox = bbox.astype(float)
        self.hits = 1
        self.missed = 0

class PersonTracker:
    def __init__(self, iou_thresh:float = 0.3, max_age:int = 30, min_hits:int=3):
        self.iou_thresh = float(iou_thresh)
        self.max_age = int(max_age)
        self.min_hits = int(min_hits)
        self.next_id = 1
        self.tracks:List[Track] = []
        self.unique_confirmed:Set[int] = set()

# 1. 입력 dets(검출 바운딩 박스)와 기존 self.tracks(추적 트랙) 사이의 IoU(Intersection Over Union:겹친부분 / 보이는 부분 전체)를 기준으로 1:1 greedy 매칭 수행
#    각 검출(detection)은 최대 하나의 트랙과만 연결될 수 있음. 각 트랙 역시 최대 하나의 검출과만 연결됨
#    (greedy는 순차적으로 현재 가장 좋은(최대IoU)매칭을 선택하는 방법임.)
# 2. 각 검출을 한 번씩 순회하면서(dets 배열을 앞에서 부터 하나씩 확인함), 아직 사용ㄹ되지 않은 트랙들 중 IoU가 가장 큰 트랙을 찾음.
# 3. 그 최대 IoU가 임계값 self.iou_thresh 이상이면 (det_idx, track_idx)를 매칭으로 확정하고, 해당 검출/트랙을 재사용하지 않도록 표시함.
# 4. 매칭에 실패한 검출 인덱스와 트랙 인덱스를 각각 unmatched_dets, unmatched_tracks로 반환함.
#    unmatched_dets : 현재 프레임에서 새로 검출된 바운딩 박스 중, 어떤 트랙과도 매칭되지 못한것들.
#                     해당 검출이 새로운 사람일 가능성 -> 이 인텍스에 해당하는 검출 박스들로 새로운 트랙을 생성함.
#    unmathced_tracks : 이전 프레임에서 추적 중이던 트랙 중, 이번 프레임에서 어떤 검출과도 매칭되지 못한것들.
#                       이 트랙드은 lost상태를 표시되면, 일정 프레-임이상 계속 매칭이 안되면 삭제됨.
#                       반대로 몇 프레임 동안 누락되었다가 다시 검출되면 재매칭될 수 있음.

    def _match(self, dets: np.ndarray) -> Tuple[List[Tuple[int, int]], List[int], List[int]]:
        matches = []
        if len(self.tracks) == 0 or len(dets) == 0:
            return matches, list(range(len(dets))), list(range(len(self.tracks)))
        used_tracks = set()
        used_dets = set()
        for di, db in enumerate(dets):
            best_iou, best_ti = 0.0, -1
            for ti, trk in enumerate(self.tracks):
                if ti in used_tracks:
                    continue
                iou = iou_xyxy(db, trk.bbox)
                if iou > best_iou:
                    best_iou = iou
                    best_ti = ti
                if best_ti >= 0 and best_iou >= self.iou_thresh:
                    matches.append((di, best_ti))
                    used_dets.add(di)
                    used_tracks.add(best_ti)
            unmatched_dets = [i for i in range(len(dets)) if i not in used_dets]
            unmatched_tracks = [i for i in range(len(self.tracks)) if i not in used_tracks]
        return matches, unmatched_dets, unmatched_tracks

    def update(self, dets:np.ndarray) -> List[Track]:
        matches, unmatched_dets, unmatched_tracks = self._match(dets)
        
        for di, ti in matches:
            trk = self.tracks[ti]
            trk.bbox = dets[di].astype(float)
            trk.hits += 1
            trk.missed = 0
            if trk.hits >= self.min_hits:
                self.unique_confirmed.add(trk.tid)
        
        for ti in unmatched_tracks:
            trk = self.tracks[ti]
            trk.missed += 1

        self.tracks = [t for t in self.tracks if t.missed <= self.max_age]

        for di in unmatched_dets:
            t = Track(self.next_id, dets[di])
            self.tracks.append(t)
            self.next_id += 1
        return self.tracks
    
    def unique_count(self) -> int:
        return len(self.unique_confirmed)
    
def draw_boxes_with_ids(frame_rgb: np.ndarray,
                        tracks:List[Track],
                        overlay_text:str) -> np.ndarray:
    img = Image.fromarray(frame_rgb)
    drw = ImageDraw.Draw(img)
    font = ensure_font()

    for trk in tracks:
        x1, y1, x2, y2 = [float(v) for v in trk.bbox]
        drw.rectangle([x1,y1,x2,y2], outline=(0,255,0), width=3)
        tag = f"ID {trk.tid}"
        l, t, r, b = drw.textbbox((0,0), tag, font=font)
        tw, th = (r-l), (b-t)
        top = max(0.0, y1 - th - 6)
        drw.rectangle([x1, top, x1+tw+8, y1], fill=(0,255,0))
        drw.text((x1 +4, top + 2), tag, fill=(0,0,0), font=font)
    
    if overlay_text:
        l,t, r, b = drw.textbbox((0,0), overlay_text, font=font)
        drw.rectangle([5,5,5 + (r-l) + 14, 5+(b-t) + 14], fill=(0,0,0))
        drw.text((12,12), overlay_text, fill=(255,255,255), font=font)

    return np.asarray(img)

# CNN.py --model C:\AIClassSecondRun\python\CNN\yolov8s.pt --video-in C:\AIClassSecondRun\python\CNN\airport.mp4 --video-out \\output.mp4 
def main():
    ap = argparse.ArgumentParser()
    # ap.add_argument("--model", required=True, help="YOLO 모델 경로 또는 별칭(예: yolov8s.pt)")
    # ap.add_argument("--video-in", required=True, help="입력 영상 경로 (mp4 등)")
    # ap.add_argument("--video-out", required=True, help="출력 mp4 경로(예: \\output.mp4)")
    ap.add_argument("--model", default=r"yolov8s.pt", help="YOLO 모델 경로 또는 별칭(예: yolov8s.pt)")
    ap.add_argument("--video-in", default=r"C:\AIClassSecondRun\python\image\subway-inside.mp4", help="입력 영상 경로 (mp4 등)")
    ap.add_argument("--video-out", default=r"C:\AIClassSecondRun\python\CNN\output2.mp4", help="출력 mp4 경로(예: \\output.mp4)")
    ap.add_argument("--conf", type=float, default=0.30, help="신뢰도 임계값")
    ap.add_argument("--iou", type=float, default=0.50, help = "NMS IoU 임계값")
    ap.add_argument("--device", type=float, default=None, help="예: 'cpu' 또는 '0'(GPU)")
    ap.add_argument("--macro-block-size", type=int, default=3, help="FFmpeg macro block size")

    # 트래커 하이퍼 파라미터
    ap.add_argument("--track-iou-thresh", type=float, default=0.3, help="트랙-검출 매칭 IoU 임계값")
    ap.add_argument("--max-age", type=int, default=30, help="미관측 허용 프레임 수")
    ap.add_argument("--unique-min-hits", type=int, default=3, help="유니크 확정 최소 연속 관측 수")
    
    args = ap.parse_args()
    print(args)

    # 모델, 클래스
    model_path = resolve_model_source(args.model)
    model = YOLO(model_path)
    class_names = get_class_names(model)
    person_idx = class_names.index("person")

    # 비디오 IO
    reader = imageio.get_reader(args.video_in)
    meta = reader.get_meta_data() # fps, size(폭, 높이), nframes(총 프레임 수), duration
    fps = float(meta.get("fps", 30.0)) # fps 정보가 없으면 기본값으로 30.0
    writer = imageio.get_writer(
        args.video_out, 
        fps=fps, 
        codec="libx264", 
        quality=8, 
        macro_block_size=args.macro_block_size # H.264, quality(0~10) 
    )

    # 트래커/통계
    tracker = PersonTracker(
        iou_thresh=args.track_iou_thresh, max_age=args.max_age, min_hits=args.unique_min_hits
    )

    frames_processed=0
    total_person_boxes = 0
    failed_reads = 0

    try:
        for idx, frame in enumerate(reader):
            frames_processed += 1

            # pred는 YOLO 모델이 한 프레임에 대해 반환한 Results 객체임
            # pred.boxes는 해당 프레임에서 검출된 모든 객체의 바운딩 박스 모음임
            # dets에 들어가는 값은 pred.boxes에서 추출한 박스 좌표 배열임.
            # [0]은 1장의 이미지가 입력되었기 때문임. [Results]

            pred = model.predict(
                source=frame, conf=args.conf, iou=args.iou, device=args.device, verbose=False
            )[0]

            if pred.boxes is None or len(pred.boxes) == 0:
                tracker.update(np.zeros((0,4), dtype=float))
                overlay = f"unique: {tracker.unique_count()} active: {len(tracker.tracks)} frame: {idx}"
                annotated = draw_boxes_with_ids(frame, tracker.tracks, overlay)
                writer.append_data(annotated)
                print(f"Frame {idx}: 0 person boxes, unique_total={tracker.unique_count()}, active_tracks={len(tracker.tracks)}")
                continue

            boxes = pred.boxes.xyxy.cpu().numpy() # YOLO 검출결과의 박스 좌표를 NUmpy 배열 (N*4)로 얻는 체인임
            confs = pred.boxes.conf.cpu().numpy() # YOLO 검출 결과에서 각 객체의 confidence(신뢰도) 값을 Numpy 배열로 뽑아냄.
            clses = pred.boxes.cls.cpu().numpy().astype(int) # YOLO 검출 결과에서 클래스 ID들을 Numpy 정수 배열로 뽑아냄. 0=person

            keep = (clses == person_idx) & (confs >= args.conf)

            if not np.any(keep): # 사람을 검출한 뒤, keep에 맞는 사람이 하나도 없는 경우에
                tracker.update(np.zeros((0,4), dtype=float)) # 박스가 0개인데 형식은 [x1,y1,x2,y2] 좌표구조임
                overlay = f"unique: {tracker.unique_count()} active: {len(tracker.tracks)} frame: {idx}"
                annotated = draw_boxes_with_ids(frame, tracker.tracks, overlay)
                writer.append_data(annotated)
                print(f"Frame {idx}: 0 person boxes, unique_total={tracker.unique_count()}, active_tracks={len(tracker.tracks)}")
                continue

            person_boxes = boxes[keep]
            total_person_boxes += person_boxes.shape[0]

            active_tracks = tracker.update(person_boxes)
            overlay = f"unique: {tracker.unique_count()} active: {len(active_tracks)} frame: {idx}"
            annotated = draw_boxes_with_ids(frame, active_tracks, overlay)
            writer.append_data(annotated)

            print(f"Frame {idx}: {person_boxes.shape[0]} person boxes, unique_total={tracker.unique_count()}, active_tracks={len(active_tracks)}")

    finally:
        try:
            writer.close()
        except Exception:
            pass
        try:
            reader.close()
        except Exception:
            pass

    print(f"[OK] saved: {args.video_out}")
    print(
        "[SUMMARY]"
        f"frames_processed={frames_processed}, total_person_boxes={total_person_boxes},"
        f"unique_persons={tracker.unique_count()}"
    )

    import json, os
    summary = {
        "frames_processed":int(frames_processed),
        "total_person_boxes":int(total_person_boxes),
        "unique_persons":int(tracker.unique_count())
    }

    # 원자적(atomic) 저장: 임시 파일에 쓴 후 교체
    tmpfile = "aummary.json.tmp"
    dstfile = "summary.json"

    with open(tmpfile, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    
    os.replace(tmpfile, dstfile)
    print(f"[SUMMARY] saved to {dstfile}")

if __name__ == "__main__":
    main()