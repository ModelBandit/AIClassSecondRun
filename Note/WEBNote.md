LLM, 웹 - Agent
서블릿

semantic tag - html5에서 나온거

href

homepage / was (Web App Server)
HTML,css,js / Web App Server
메뉴버튼(인풋같음) / 로그인 (사용자따라 인풋이 다름)

Tomcat server -> hp나 was를 한번에 작성해줌

Chart JS - 화면에 뿌려줌? UI?

WAS가 DB에서 ML에 접근

asyncd 프로그램 - DB를 통해 정보를 끌어올떄 필요

servlet - server + applet

폰트사이즈 pt px 있지만 웹에서는 px

캐러셀? 메인에 큰화면있고 좌우버튼 누르면 배경전체가 바뀌는 형태

실전에서는 JSP 위주로 됨. 진저나 다른건 장난감용

OS achitecture network

ajax 비동기 프로그램

hidden tag의 중요역할
csrp - Cross Site Request Forgery
csrp 방지를 위해서 토큰사용

보안문제로 쿠키에서 세션으로 옮겨감

ID값은 해당 페이지(div,p)를 js로 유동적 컨트롤하는데 사용

aliment? endian과 관련?

js - echma6오면서 코드처럼 바뀜
대표적인 백엔드는 node.js
풀스택이였다면 react도 했을 것

Java Server P
JSP -> surblat(JSP)
UI가 복잡한 상황에서는 성능을 많이 먹음(동영상이 많다던가)

아트 머시기를 써서 하는게 Deep Learning (Neural Network)
CNN RNN Transfomer(인코더 디코더), 구글논문(디코더만 필요)-> llama

classfication
분류/회귀 였나 그랬음
prediction

agent는 강화학습을 통해서 학습하는데 거기에 markov process를 사용함.

js 생명줄: ajax(비동기가능)을 통한 jquery. echma6의 패치api를 써야하는데 보통 기본 제공

ajax, fetchAPI로 붙인다. 어디에?

project object model -> xml 사용처

GIS?

리눅스의 라우터데몬을 보면 매커니즘은 확인 가능
다이젝스트라가 기본원리

defacto -> tcp/ip

transmission connect
tcp/ip : connection oridented된 상태로 작동한다
udp : connectionless
user datagram protocol

transmission
TCP - flow control(주고받는 속도 컨트롤) *(Slide Window (점점 많이 보내는 방식))
       error handleing(데이터 잘 받았는지 확인함(UDP는 안함))
-------------------------
network(IP) - 라우터
---------------------------
data(스위치장비) - CSMA 802.3 - 멀티콜리전 발생시, 재전송하는 프로토콜
-------------------------
physics - 하드웨어

packet = header+payload

포트넘버도 암묵지가 있음

header = []

CRC16 

개인끼리 애니캐스트
그룹끼리 멀티캐스트
멀티캐스트 - 브로드캐스트(ARP Address Resolution, 대충 생존신고하는 프로토콜)

서버
Web - 퍼블리셔영역
WAS - 개발자영역

홈페이지 제작 - 아파치(리눅스도 여기)

처음접속하면 DNS서버로 접속함

app과 web의 차이 - 지금하는건 웹

was서버가 톰캣을 통해서 servlet으로 컨버전되면 JSP

SOAP이 너무 무거워서 MSA로 전환됨

서버 대 서버는 URI로 붙임

뷰는 자바로
컨트롤은 서블릿 - 우리는 스프링에 디스페쳐써서 처리할것

포맷을 명시해놔도 인력이슈로 포맷문제가 발생할 수 있어서 filter(기법)를 사용하는게 도움이 될 수 있음

템플릿 엔진

타임리프 - 미국 권장사항(근데 한국은 안씀)

스프링 부트를 JSP에서 쓰려면 추가작업 필요

문제 발생시 자바/톰캣/서블릿인지 구분할 줄 알아야함

톰캣9이 뭔가 처리해줌

다른 서블릿 (.=. 다른 클래스)

만약 request, response 이해가 어렵다면 서블릿에 대한 지식이 필요할 것
서블릿의 일종을 디스페쳐가 만듬

요구사항 정의서의 id를 기반으로 프로그램 점검됨(갑이)

UI개발 가급적 동적으로 할것(정적인거 사용량 줄일것)
정적이면 그건 홈페이지임
우리는 WAS를 해야하니 주의할 것
다이나믹하게 프로세싱해서 동적인 결과를 출력해야함

스프링의 컨테이너 개념****

chart.js같은 경우 pathAPI(요즘꺼)나 ajax를 이용해서 비동기로 짜야함

파이썬이 멀티쓰레드가 지원이 안되는 원인 JIL?

폼태그로가서 데이터를 서버로 쏘면 그걸 톰캣이 잡고 컨트롤러로 넘기고 스프링에서 메소드를 불러옴

SQLite는 파일형태로 저장됨

현업에서는 퍼포먼스 문제로 프론트랑 백에 각각 was를 세워서 처리함

주소를 막치고 들어간 다음
Context root - 흔히 트리의 루트에서 사용하는 그 트리는 맞음. 보통 프로젝트 이름이랑 같게함
content directory - 말 그대로 이미지나 텍스트같은 컨텐츠 들어있는 라인. 그래서 제너레이트 필요

jsp 생성시 포맷설정 중요함.
연습해보면 EUC-KR로 돼있을텐데 UTF-8로 맞춰서 통신해야함.