Unit Test: 단위 테스트 - 내꺼만 돌리는거
Total Test: 통합 테스트 - 병합후 전체 플로우 테스트

JUNIT: 개발자가 JUNIT을 돌려서 걸리면 해당 오류 수정까지 개발을 막는 방법
TDD(Test Driven Development): 테스트 주도 개발

as: 리눅스의 개념. alias 의 약자.

파일을 open()으로 호출하면 os를 통해서 file descriptor가 나옴

open close를 기본적으로 쓰긴하지만 with키워드를 쓰는 경우 close를 컴퓨터가 관리함

try-except를 여러개 써도 되는 경우 - 하나의 인풋이 여러 타입을 받을 수 있을 때

pass로 인한 문제
1. 에러가 숨겨짐 - 위치파악이 어려움, 알게모르게 허점이 쌓여감
2. 디버깅 불가능 - 에러 메세지 출력이 없어서 추적이 어려움
3. 코드 관리가 불가능 - pass로 넘어갔기에 작성자를 제외하고 의도 파악이 불가능함.

Most signity bit (최 좌측 비트) - 음수 양수 표현해줌
나머지 7비트를 영어로 채울수 있으니 거기에 영어로 채워서 표현

ASCII(American Standard Code for Information Interchange)

filter(조건 함수, iterable)로 돌아가는 함수. 이름 그대로 걸러줌

type(primitive - object): 보통 원시타입과 객체타입으로 번역되며 immutable mutable로 불변형, 가변형으로도 불림
다른데는 아니지만 파이썬은 primitive가 없으니 참고

truncate

fillment

환경 변수(Environment Variable)란 프로세스가 컴퓨터에서 동작하는 방식에 영향을 미치는, 동적인 값들의 모임
└ cmd에서 디렉토리 없어도 이름만 써서 연결해주는 그거

프로그램 - 하드 디스크에 있는 것, exe -> 프로세스: 실행되고 있을 때
쓰레딩 - 하나의 환경에서 여럿이서 동작하는 것

여러개의 코어?(왜 메모리라고 써뒀지?)를 쓰면 멀티쓰레드

공유자원은 힙메모리에 있는 객체만 해당되고 스탭은 안됨(아마 파이썬 특성)

Inter Process Communication IPC - 하나의 프로그램에서 프로세서간 통신하는 것