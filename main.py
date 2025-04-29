from abc import ABC, abstractmethod

# abstractstaticmethod랑 abstractclassmethod가 있었는데 3.3이후로 폐지 됐지만 남아는 있음
# 이름따라서 static method랑 class method였을 듯 함.
# static은 getter setter랑 abstractmethod랑 겹쳐서 사라지고
# class는 classmethod와 abstractmethod로 나눠져서 소멸함

# ABC 달아주고 나서부터 데코레이터로 인한 강제성이 생김
class Dog(ABC):
    @abstractmethod
    def printInfo(self, kindString):
        pass

class Chihuahua(Dog):
    def printInfo(self): # 인자는 굳이 맞추지 않아도 됨
        print("야는 치와와여")

class ChowChow(Dog):
    def printInfo(self, string1, string2):
        print(f"사실 여기 차우차우는 없어...\n그냥 {string1}과 {string2}를 보여주고 싶었어.")

dog1 = Chihuahua()
dog2 = ChowChow()

dog1.printInfo()
dog2.printInfo("충격", "공포")