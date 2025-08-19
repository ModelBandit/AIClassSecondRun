import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import os

os.environ["PATH"] += os.pathsep + r"C:\ffmpeg-2025-08-18-git-0226b6fb2c-full_build\bin"

device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-large-v3-turbo"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)
processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    torch_dtype=torch_dtype,
    device=device,
    return_timestamps=True,
    chunk_length_s=10,
    stride_length_s=2,
)

path = r"C:\AIClassSecondRun\python\sound.mp3"

result = pipe(path)

print(result)