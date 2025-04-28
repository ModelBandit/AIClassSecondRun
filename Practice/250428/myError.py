class MyError(Exception):
    def __str__(self):
        return "개쩌는 에러의 세계"

class Bird:
    def fly(self):
        raise MyError
    
class Eagle(Bird):
    pass

eagle = Eagle()

try:
    eagle.fly()
except MyError as e:
    print(e)