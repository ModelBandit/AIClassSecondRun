st1 = "python"
st2 = "Test"

su = 100

flt = 11.11

num = '110'

# print(flt+su)
# print(st1 + st2)
# print(su+num)

print("type su: ", type(su))
print("str su: ", type(str(su)))
print("float su: ", type(float(su)))
print("type su: ", type(su))

#실수에서 정수로 형변환 불가
num = "0101"
print(int(num))

# str, float, int를 캐스팅 함수(연산자)라고 표현
# 캐스팅 함수를 이용해서 강제 형변환을 할 수 있다.
# 캐스팅 함수를 사용하면 단발성이지만 변수에 저장하면 완전 속성을 변경 가능하다.

# 숫자형 간의 연산자 사용시 덧셈으로 진행됨
# 시퀀스형 자료형은 + 연산자를 사용하면 하나로 합쳐주는 업데이트 연산이 진행된다.

# 단, 시퀀스형 자료형 연산은 좌, 우 피연산자의 자료형이 일치해야 한다.
# ※ 시퀀스형 자료형이란
# 0~n-1의 보조첨자를 사용하며, 자에서 우로 순서가 존재하며, 반복문에서 차례대로 대입되는 속성을 가진 자료형

# flt = 123.456

# print("round(flt) : ", round(flt) )
# print("round(flt, 1) : ", round(flt, 1) )
# print("round(flt, 2) : ", round(flt, 2) )


# 앞에 20자리 공백을 넣어주고 앞 3칸만 출력됨. 매우 트릭키함
# print(f"{"[%20.3s]" % "suzan strong"}")

# print("default : %f5" % 123.45678)
# #%A.Bf 에서
# # A는 소수점을 포함한 전체 칸확보 수
# # B는 표현할 소수자리 지정(단, 반올림 처리되어 출력됨)
# print("set value : %10.3f" % 123.45678)
# print("set value : %2.1f" % 123.45678)
# print("set value : %.2f" % 123.45678)

# #fstring 지정식 표현. 서식제어문이 아니라 %표시는 안됨
# print(f"{123.123123123:.2f}")

# print("%c %c" % ('a', "A"))
# print("%c %c" % (97, 65))

# print("%d" % 123)
# # print("%d %d" % 123)
# # print("%d" % (123, 321))
# print("%d %d" % (123,321))
# print("%d + %d = %d" % (123,321,123+321))

# print("%lf" % 123.123654987456321)

# print(0b01111011)
# print(0o173)
# print(0x7b)
# print(123)

# print(f"12 + 54 = {12+54} 입니다")
# print(f"268 - 42 = {268-42} 입니다")
# print(f"2 * 23 = {2*23} 입니다")
# print(f"120 / 3 = {120/3} 입니다")

# print('표현 \ 방식')
# print('표현 \1 방식')
# print('표현 \2 방식')
# print('표현 \3 방식')
# print('표현 \4 방식')
# print('표현 \5 방식')
# print('표현 \6 방식')
# print('표현 \7 방식')
# print('표현 \8 방식')
# print('표현 \9 방식')
# print('표현 \10 방식')
# print('표현 \\2 방식')
# #print('표현 방식\') #error code
# print('표현 방식\\')

# print("11111111111111111111111111111111111111111111")
# print("Have\t""a\t""Good\t""Time.")
# print("1234567\t""1\t""12345678\t""123")
# print("ㄷㄷㄷㄷ\tㅁㄷ\tㅁㄴㅇㄷㄷㄷ\t응애")


# Unmananged 언어
# 하드웨어를 수동 제어각 가능하다.
# 주로 운영체제난 유틸리티 제작에 사용된다.
#     다만 인지도가 높아서 보안에 취약
# 어려움


# managed 언어
# python, java
# 하드웨어를 자동관리한다.
# 주로 큰 작동을 담당하면서 메모리 관리가 필요한경우
# 다른언어와 조합해서 사용한다. 접착성 - python
# 쉽다.


