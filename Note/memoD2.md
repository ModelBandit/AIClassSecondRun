클래스

(생성한 객체는) 고유한 성질을 가짐

(생성한 객체는) 서로에게 영향을 주지않음

→ 할당된 공간이 다르니까

SRP - Single Responsbility Principle

단일 책임 원칙

### MVC 패턴 - Model View Controller

**Model = DB**

**View = UI**

**Controller = 라우트 배치 (플로우 설정)**

이렇게 역할를 3가지로 역할을 분담하여 프로젝트를 진행하는 방식

- **Model**
    - 데이터를 담당하는 부분 (DB)
    - 다른 두 역할이 Model에게 일방적인 통신이 이루어짐
- **View**
    - User Interface를 담당
    - Model에서 데이터를 뽑아와 사용자에게 표시
    사용자의 입력은 Controller에게 전달
- **Controller**
    - 전체적인 데이터의 플로우를 관리함.
    - 전달된 입력을 처리하고 Model을 조작하거나 업데이트하고 그 결과를 뷰에게 전달한다.

상속: 부모 클래스를 프레임으로 자식 클래스를 생성함

→ 즉, 자식 클래스 들의 공통점을 모아둔 클래스가 부모 클래스 → 이렇게 처리하면 일반화

[클래스 객체 관계]

객체는 다른 객체와 관계를 맺게됨

- 집합 관계: 완성품과 부품 관계(Composite Pattern) - 차와 바퀴
- 사용 관계: 객체가 다른 객체를 사용하는 관계(연관 관계, Association) - 사람과 계산기
- 상속 관계: 객체간의 부모-자식 관계 (일반화 관계, Generalization) - Animal과 Dog, Bird와 같은 관계

 

오버라이딩: 상속받은 클래스가 상속 함수에 새로운 기능을 추가하거나 변경하는 것

IS A 관계 점검: 잘못된 상속 관계를 도출하는 기법 Dog is A Chihuahua는 될수 없지만 Chihuahua is a Dog는 될수 있는 원리

UML(Unified Modeling Language) 

파인튜닝 (Fine Tuning): 사전에 학습된 모델(Pre Training)을 용도에 맞게 조정하는 과정.
가장 일반적인 생성형 ai 모델 딥러닝 기법

프리트레이닝 (Pre Traning): 모델 이라고 불릴수 있는 파일을 만드는 작업. 지금 아는 정보에 한해서는 대화가 가능한 형태를 취해야 함. 

SQLlite는 스마트폰용, 빅데이터를 감당이 불가능 → 오라클을 선정한 이유

접근 제한자: 파이썬에는 따로 존재하지 않고 _(언더바, 언더스코어) 1개, 2개로 제한 등급을 올림.

경우에 따라 이름이 겹치는 경우를 방지하기 위해서 **_클래스이름__변수** 같은 식으로 내부적으로 변경된다. 이렇게 **클래스가 정의되는 시점에서 내부적으로 필드나 메서드의 이름이 변경되는 메커니즘**을 **네임 맹글링**이라고 부른다. 본의 인지는 모르지만 이를 통해서 private인 멤버에도 접근이 가능하다.

상속하여 반드시 재작업을 해야되는 경우 인터페이스쪽이 더 좋음(상속보다 인터페이스가 좋다는 말의 의미)

- 상속 시, 부모와 자식 둘 다 힙에 배치됨

```python
class Parent:
    def __init__(self):
        self.__value = "부모"

    def show(self):
        print(self.__value)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__value = "자식"

c = Child()
c.show() # 힙에는 Parent랑 Child가 둘다 존재함. 그리고 이 두개가 둘 다 초기화 된 상황
         # 거기에 show함수가 상속 되어서 사용은 가능하지만
         # 자식의 value에 접근하는 함수가 아니기에
         # 부모의 value를 출력하게 됨
print(c.__dict__)# 갑자기 매직키워드?
```

- 만약 복수의 자식 객체가 생성된 경우

```python
class Parent:
    def __init__(self):
        self.__value = "부모"

    def show(self):
        print(self.__value)

    def setter(self, value):
        self.__value  = value

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__value = "자식"

class OtherChild(Parent): # Parent를 상속받는 다른 자식 클래스 생성
    def __init__(self):
        super().__init__()
        self.__value = "다른 자식"
        super().setter("바스타드")

c = Child()
oc = OtherChild()
c.show() # 이전과 같이 "부모"가 출력
oc.show() # "바스타드"가 출력
# 이로 미루어 볼때 상속 개체를 생성할 때마다 부모-자식이 한 세트로 힙에 잡히는걸로 보임.
# 부모|자식|다른자식 으로 메모리를 할당하는게 아니라
# 부모|자식 ..떨어진 어디간.. 부모|다른자식으로 별개의 부모가 생성됨
```

- 메모리 상에서 같은 부모를 사용하고 싶은 경우

싱글톤으로 해결할수 있을거같은데….주말에 올리도록 하자.

상위 클래스의 골자를 상속받은 하위 클래스가 사용할 수 있게 하는 동작. 대상은 언더바 1개 이하**(public protected)**의 접근제한을 걸어둔 필드나 메소드가 상속되며 코드의 중복을 줄여 **개발속도와 유지보수 편리**성을 제공하며 **다형성이 구현**된다.

Dog dog = new Chihuahua()가 가능하다.

이런 식으로 **부모 클래스에는 모든 자식 클래스가 대입**될수 있어 **객체를 부품화** 시킬 수 있게되고 인터페이스(전부 추상화된 클래스)의 경우에는 **모든 구현 객체가 대입**이 가능하여 **기능 확장 및 변경에 용이**하다. 또한 추상화된 대상은 힙에 생성되지 않음. 재정의 없이 다시 상속되는 경우에도 힙에 생성되지 않음

생성자 / 소멸자: __new__+__init__ / __del__

@abstractmethod 데코레이터를 클래스 내 함수 상단에 사용하게 되면 해당 함수는 가상 함수로써 반드시 재정의 해야하는 함수로 취급됨. 이런 함수를 포함하는 클래스를 가상 클래스라 칭함.

만약, 클래스에 추상화 함수만 채운다면 이는 인터페이스라고 불림.

상속화 = 컴포넌트 베이스 = 모듈화

전략패턴 strage 적용시 interface가 효과적