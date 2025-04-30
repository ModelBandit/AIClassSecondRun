# 치송.Day01

**OOP** = object oriented programming

**SQL** = oracle, mysql은 보안상 문제가 있음

**RAG** = LLM 검색기능, Retrievar Agumented증강 Generation 

**cpu**에 따라서 **기계어**가 다름 - 이를 **컴파일**과정에서 맞춰주는것

파이썬은 데이터를 전부 힙으로 올린다? - 하단 참조

**스택:** **컴퓨터**가 관리하는 메모리

**힙:** **개발자**가 런타임 중 동적으로 할당받아 관리하는 메모리
└ 메모리파트에 질문 ┐
파이썬에서 **선언된 변수**는 **스택**에 올라가고
class()같은 식으로 **객체를 생성**하는 순간 이건 **힙**에 올라감.
즉, c = class()로 작성한다면 c는 스택 class()는 힙으로 올라가며 c는 포인터로써 class()가 있는 힙을 가르킴

### 인스턴스 ⊆ 객체 ⊆ 클래스

**클래스 ****- 똑같은 무언가를 계속 만들어 낼 수 있는 설계 도면
└ 사물과 추상 : 변수와 메소드로 치환됨

**ex)—————————————**

class Dog():

def __**init—**(self, string):

self.name = string

print(f”이 개는 {self.name}이다.”)

# class를 구상하고 선언함.

**e——————————————-**

**객체 ****- 클래스로 생성한 실체

└ 객체가 생성되고 메모리에 할당되어 실제로 사용됨

**ex)——————————————-**

chihuahua = Dog(”Chihuahua”)  # 객체를 생성한 것

**e————————————————-**

**인스턴스** - 객체가 어떤 클래스인지 실체를 명확히함.

└ 특정 클래스에서 생성된 객체임을 강조할 때 씀.

**ex)—————————————————**

#생성이 되고 메모리에 올라간 뒤,(이때부터?)

#생성자가 호출되어 터미널에서 print로 인하여 문자가 출력되었다.

**e———————————————-**

### 정리——————————————

명제: ***“chihuahua라는 객체”***는 ***“Dog 클래스의 인스턴스”***이다.
인스턴스 = 어떤 클래스인지 실체를 명확히 한다.

즉, 클래스의 기준에서 객체를 본다면 객체는 인스턴스로 칭한다.

### 정리끝—————————————-

**ORM** - 클래스째로 db에 매핑하는 기법

**스택 프레임** - 함수를 호출하게 되면 메모리 상에 해당 함수와 함수의 지역 변수가 들어앉는 공간이 스택 메모리에 할당됨. 이렇게 **하나로 묶인 스택 메모리 공간**을 스택 프레임이라 칭함

클래스 내 변수 - 필드
클래스 내 함수 - 메소드

파이썬 값 전달 방식

call by value / call by reference

immutable / mutable

**Value**타입: 값만 불러오기에 새로 복사생성되어 스택에서 하나 힙에서 하나씩 새로 생성하게 됨.

즉, 추가 메모리를 필요로함.

**Reference**타입: 같은 주소의 메모리 공간을 같이 사용함. 파이썬의 메모리 할당 방식대로라면 스택만 할당하고 힙은 따로 할당하지 않음. 그래서 스택 메모리에 하나 더 생기지만 힙 메모리 사용량에는 변화가 없음.

global 선언시 global namespace라는 별도 **딕셔너리** 공간에 저장됨

이렇게 등록된 변수는 globals()로 접근하여 확인할 수 있다.

네임스페이스: 이름과 객체를 매핑하여 구분해둔 범위

컴퓨터 구조는 폰 노이만 구조를 취함

지금이야 메인보드, cpu, ram, HDD(SSD), IO 등등있지만 기본적으로 CPU, 메모리, 프로그램으로 구성. CPU가 돌아가며 연산을 처리하고 연산하는 정보들을 메모리에 얹어서 두며 프로그램을 통해 지시를 내리는 구조. 점점 다른 장치들이 추가되어왔지만 기본적으로 저 세가지를 기반으로 굴러가는 기본 골자는 그대로임

**CPU와 GPU의 차이**

CPU (Central Processing Unit): 중앙 처리 장치. 이름 그대로 컴퓨터가 돌아가는 **모든 연산에 관여**한다. 터미널을 통해서 지시된 작업을 **순서대로 처리**하며 **단일 코어가 빠르게 동작함.**

GPU (Graphic Processing Unit): 그래픽 처리 장치. 그래픽 관련된 연산을 담당함. 대체로 **코어가 많은편**이고 **CPU에 비해 그리 빠른편은 아님**. 코어가 많은 덕에 **병렬처리에 특화**되어 있음. 기본적으로 컴퓨터에 모니터랑 연결되는 잭있는 부분에 **내장 GPU**가 있어서 디스플레이를 위해 동작함. **외장 GPU**의 경우, NVIDIA사나 AMD사가 투탑으로 뛰고있음. **독립적인 메모리**를 가지고 있고 **내장 GPU보다는 확실히 빠르지만 여전히 CPU에 비빌 속도는 안나옴**. 다만 **코어 수가 상당하기에 병렬 연산 속도가 남다름**. 흔히 **AI에 GPU가 활용되는 부분이 이 대규모 병렬처리를 필요**로함.

**함수화가 캡슐화에 어떤 도움이 되는지**

└ 먼저 정리할 사항: 캡슐화로 얻는 것.

1. 데이터 보호 / 은닉 - 내부의 데이터를 함부로 조작하지 않게함.
2. 확장성 - 코드의 추가/수정이 편함. (추상화나 상속, 다형성이 여기 속함)
3. 유지보수 - 코드 변경이 이루어질 때, 위험은 최소화함.
4. 인터페이스 제공 - 함수를 통해 해당 클래스와 상호작용 하도록 설계함.
- 이 4가지가 유기적으로 연결된 형태를 취함. 어떤 하나를 신경쓰면 다른 하나가 본의 아니게 지켜지고 그럼.
- 만약 __num에 접근하기 위해 함수화를 시도한다면 getter, setter함수를 작성하게 됨.

class ParentClass:

# 해당 데코레이터(**@absractmethod**)를 넣어주면 해당 함수는 가상 함수로 취급되어 상속되는 함수는 반드시 이 함수를 만들어야 함. 안하면 터짐.

@absractmethod 

def getter():

pass

@absractmethod

def setter(value):

pass

class MyClass(ParentClass):

__num = 0

def getter():

return __num

def setter(value):

__num = value

이런 클래스를 작성하는 경우, 인터페이스 제공을 신경썼다면 본의 아니게 함부로 데이터를 조작하지 않고 해당 함수를 통해서만 조작하기 때문에 어느정도의 보호 효과를 제공하게됨. 반대로 접근하는 경우도 마찬가지. 거기에 만약 추상화된 함수가 있는 클래스를 상속 받았다면 이는 일관성을 높여서 확장성에도 기여를 하게됨. 개발자의 의도인지는 모르나 저 4가지 요소는 알게모르게 서로 연결되어있음.

가독성 - 작성된 코드가 얼마나 읽긴 편한지. 협업에서 많이 중요함.

## 머신러닝이란?

**아서 사무엘**

a field that enables computers to autonomouusly acquire knowledge without being explicitly programmed. (**컴퓨터가 명시적으로 프로그래밍되지 않고도 스스로 지식을 습득할 수 있도록 하는 연구 분야.**)

implecite 추상적

explicite 명시적

톰 미첼

a study of computer algorithms that allow computer program to automatically improve through experience.

(**컴퓨터 프로그램이 경험을 통해 스스로 개선될 수 있도록 하는 알고리즘을 연구하는 학문**)

Score = w * time + b

w, b를 찾아가는 과정 머신러닝

w = weight

b = bias

Programming = input + program → output

Machine Learning = input + output → program

### 머신러닝 기법에서 직접 교육하는지 여부와
직/간적적 피드백을 하는지에 따른 구분

![image.png](attachment:8c3a1517-7eb1-47e3-a997-f4b5aa62e616:image.png)

![supervising copy copy.jpg](attachment:e5d975fa-b447-4e2e-937f-11a6142fc550:supervising_copy_copy.jpg)

## 머신러닝 (Machine Learning)

- **지도학습** (Supervised Learning)
    - **분류** (Classification)
    - **회귀** (Regression)
- **비지도학습** (Unsupervised Learning)
    - **차원 축소** (Dimensionality Reduction)
    - **클러스터링** (Clustering)
- **강화학습** (Reinforcement Learning)

## 학습별 적용 분야

### 지도학습

- **분류**
    - **이미지 분류** (Image Classfication)
    - **고객 유지** (Customer Retention)
    - **신원 사기 탐지** (Identity Fraud Detection)
    - **진단** (Diagnostics)
- **회귀**
    - **광고 인기 예측** (Advertising Popularity Prediction)
    - **시장 예측** (Market Forecasting)
    - **기대 수명 추정** (Estimating life Expectation)
    - **인구 증가 예측** (Population Growth Prediction)

### 비지도 학습

- **차원 축소**
    - **구조 개발** (Structure Discovery)
    - **특징 도출** (Feature Elicitation)
    - **추천 시스템** (Recommender Systems)
    - **빅데이터 시각화** (Big data Visualization)
- **클러스터링 (밀집화?)**
    - **추천 시스템** (Recommender Systems)
    - **타겟 마케팅** (Targetted Marketting)
    - **고객 세분화** (Customer Segmentation)

**강화 학습**

- **게임 AI** (Game AI)
- **실시간 결정** (Real-Time Decisions)
- **로봇 네비게이션** (Robot Navigation)
- **작업 실행** (Learning Tasks)

프로그램의 main()에는 생략되는 인자가 있으며 *args, **kwargs고 이름은 앵간하면 고정임

함수의 인자로 **아스타리스크(*)args**를 받게되면 인자를 set으로 바인딩하여 로컬에서 사용한다.

****kwargs**도 다르진 않음

func(name=”이름”, age = 18 …) 처럼 받게되면

변수측은 키, 데이터는 밸류로써 작용하여 딕셔너리 형태로 넘겨짐

**※단순히 set, dict를 받기위해 사용하는 인자와는 관점이 다름.**

멀티쓰레드 환경에서 동시다발적인게 아니라 time sharing을 통해서 따로 이루어짐

멀티쓰레드 사용 중 경우에 따라 변수의 값이 다른게 나올수 있는 상황을 race condition이라 칭하며, 이렇게 각 쓰레드에서 같은 변수를 조작하는 경쟁 자체를 memory racing이라 부름

**lambda**: 함수화 시킬만큼 복잡하지 않거나 함수화가 불가능한 경우 사용됨