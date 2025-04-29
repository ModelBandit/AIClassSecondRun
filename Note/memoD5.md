랜 방식

CSMA CD - Carrier Sensor MA Collision Detection

token ring - IBM의 프로토콜
권한있는 유저에게만 통신권한을 주는 방식 

위 두개 관련해서 조사할 것

.class(bytecode) -> JVM -> OS

JIT (Just In Time) - JVM을 C언어로 컨버팅해줌

Busy Waiting - 

CPython도 비슷한ㄱ걸 처리해줌

cpu 점유 방법론

1. Round Robin - Fairness를 공평하게 처리 - Time Slice하여 각 cpu에 시간할당
2. prioriry - VIP 서비스같은거 - 우선도 높은 대상에게 시간을 더 줌
   └ 단점: 우선도 높은 대상이 계속 잡고있으면 Time Slice에 문제가 생김 (Starvation) -> 해결책 - Anging 기법 - 대기시간이 길어지면 다음 우선도나 다른 대상의 우선도를 높여서 Round Robin으로 처리함
즉
3. 1 + 2을 시도하는게 Aging

race condition - 다른 코어들이 같은 자원을 관리하다 행동이 겹치는 문제가
└ 그래서 Synchronization 기법으로 Lock을 통해서 다른 코어의 접근을 미연에 방지함

세마포? 아무튼 이런 기법들 많음
realtime os - 정확한 시간을 지켜야하는 환경에서 사용됨

yield

process를 돌리는 대상 processor - cpu를 이렇게 칭함
보통 1 cpu환경에서는 각 코어가 동작하여 프로세서를 돌림

fork: 현재 프로세스 상에서 자식 프로세스를 만드는 행동

DMA Direct Memory Access - 파일을 건드릴때는 CPU가 하는게 아니라 얘가 함.

prompt
Non Prompt기법

cpu가 메모리에 접근할때 가장 속도를 많이 잡아먹힘
thread pool - 그래서 할당 할 수 있는 걸 미리 만들어 둠

프로세스간 데이터가 교환되는 상황
네트워크 프로세서와 GUI출력 프로세서간 통신
하나의 공유 메모리를 만들고 그 메모리를 같이 사용하여 통신

이걸 Client-Server 모델이라고 칭함

IPC

restful service 
└ HTTP 통신 - socket 바인딩은 이 단계
└ TCP/UDP
└ IP
└ MAC Address (Media Access Control Address)
└ 물리계층

spring - flask - LLM or HuggingFace

우리가 쓰는 일반적인 통신 2가지
Connection Oriented - 통신때 에러핸들링도 맡아줘서 계속해서 완전한 통신이 이루어져야 함 - TCP
Connectinalless - 커넥션없이 무작위로 쏨 - UDP - 보이스가 여기 많이씀. 꺠져도 어떻게든 돼서

우리가 쓸 XML용도 - 스프링 세팅

구글 클라우드 문제 - 작업 환경에서의 내 IP주소를 확인할 수 없음
NGLock? 으로 구글클라우드에 접근하여 IP주소를 캐낼 수 있음

오라클 설정
오라클 + JDK를 깔아야함
대충 Java Devleopment Kit같은데 
