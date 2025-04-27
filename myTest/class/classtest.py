class myClass:
    _num = 10

    def __new__(cls, *args, **kwargs): # 생성시 호출되는 함수
        return super().__new__(cls, *args, **kwargs)
    
    def __init__(self): # 생성 뒤 가장 먼저 호출되는 함수
        self.num = 5

    def __del__(self): # 카운팅 참조 순위를 올려주는 함수
        print("Calling delete")

    def func(self, num):
        self.num = num

mc = myClass()

print(id(mc))
print(id(myClass))
print(id(mc.__class__))

myClass.num = 100
print(mc.__class__.num)
print(mc.__class__._num)

#MSA MicroSoft Ahitecture

# QoS Quarity of Service 유저에 따라 서비스 품질을 나눔

# 파이썬의 메모리 접근 우선 순위와 LEGB 규칙
# └ 파이썬은 변수를 찾을때 LEGB규칙에 따라 스코프를 확인함.
#  스코프: 다른 언어의 생존주기. 블럭같은거. 접근이 가능한 구간이 정해져있다는 얘기

# Local: 함수 내부의 로컬 스코프에서 찾음
# Enclosing: 중첩 함수의 외부 함수 스코프에서 찾음
# Global: 모듈의 전역 스코프에서 찾음
# Built In: 파이썬 내장 스코프에서 찾음
#딱 봐서는 그냥 가까운데부터 찾는다는 얘기로 보임
