# from functools import reduce

# data = [1,2,3,4,5]
# result = reduce(lambda x,y : x+y, data)
# print(result)

# from operator import itemgetter

# students = [
#     ("cjane", 55 , 'c'),
#     ("Bjane", 33 , 'b'),
#     ("Ajane", 44 , 'a')
# ]

# #               list , key=itemgetter(index)
# result = sorted(students, key=itemgetter(0))
# print(result)

# import glob
# result = glob.glob("./*.*")
# print(result)

#환경 변수나 이런저너 정보들 딕셔너리
# import os
# env = os.environ
# for k in env:
#     print(f"Key: {k} - Value: {env[k]}")

# 현 디렉토리 컨트롤
# import os
# dir = os.system("dir") #현재 위치
# print(dir)
# os.chdir("../../") # 해당 위치로 이동
# dir = os.system("dir")
# print(dir)
# dir = os.getcwd()
# print(dir)
# f = os.popen("copy con aaaaa.txt").read()#파일생성으로 확인해본 바 c:에 생성됨. 디렉토리가 c:\\인 상태로 시작하는듯함. 보고 나오는 문자를 출력함
# print(f)