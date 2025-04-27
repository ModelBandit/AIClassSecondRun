def funcTrue():
    print("Print True")
    return True
def funcFalse():
    print("Print False")
    return False

# & | 는 비트연산 이상으로 안씀

print("---& operator---")
if(funcFalse() & funcTrue()):
    print("---& operator---")

print()

print("---and keyword---")
if(funcFalse() and funcTrue()):
    print("---and keyword---")

print()

print("---| operator---")
if(funcTrue() | funcFalse()):
    print("---| operator---")

print()

print("---or keyword---")
if(funcTrue() or funcFalse()):
    print("---or keyword---")

#                         1개 이상은 받지 않음
# 인자를 하나만 받을 수 있으면 1개면 어떤 자료든 안내 문구로 활용가능
#가능
#name = input("이름 %d" %10)
# name = input([1,2,3])
# name = input({1,2,3})
# name = input((1,2,3))

# 입력함수에는 print도 포함됨
# name = input("이름 입력: ")
# age = int(input("Input Age: "))
# addr = input("Input Address: ")
# print(f"name: {name}\nage: {age}\nAddress: {addr}")


# pet = ["거북이", "타란튤라", "전갈"]

# for i in range(4):
#     try:
#         print(pet[i], "키움")

#     except:
#         print("정보없음")
#     finally: # 예외처리와 상관없이 꼭 실행되야 하는 경우에 작성됨
#         print("파이널리")

# print("exit")

# while True:
#     try:
#         n1 = int(input("integer1: "))
#         n2 = int(input("integer2: "))
#         break
#     except:
#         print("숫자로만 입력")

# try:
#     result = n1 / n2
#     print("%d / %d = %d" % (n1, n2, result))
# except:
#     print("0으로 못나눔")

# print("종료")

# n1 = 10
# n2 = 0

# try:
#     result  = n1/n2
#     print("%d / %d = %d" % (n1, n2, result))
# except:
#     print("0으로는 나눌수 없음")

# print("정상종료")

# print("두 수의 합을 구함")
# print("Input")

# ## 입력함수는 입력하는 값에 따른 에러를 최소화 하기 위해
# ## 기본 자료형을 문자열로 저장하게 만들었다.
# num1 = input()
# num2 = input()
# num3 = num1 + num2

# print("두 수의 합", num1, '+',num2,'=',num3)

# print(type(num1))
# print(type(num2))
# print(type(num3))

# print("이름 입력")
# name = input()

# print("나이입력")
# age = input()

# print(name,"님의 나이는 ",age,"입니다.") # 자체적으로 사이사이에 띄어쓰기가 적용됨
# print(f"{name}님의 나이는 {age}살 입니다")
# print()

# 사용자 인풋을 위해서라도 입력함수 학습이 필요함.

# print("Input")      # 입력함수 사용시 반드시 입력함수에 대한 안내를 해준다.
#                     #작성자는 항시 사용자를 배려하는 마음으로 프로그램을 작성한다.


# num1 = input()

# print("Input Value: ", num1)