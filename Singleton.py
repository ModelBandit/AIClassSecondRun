class SingletonBase:
    _instance = None
    def __new__(cls):
        if super()._instance == None:
            super()._instance = super().__new__(SingletonBase)
        return super()._instance

class Parent(SingletonBase):
    def __new__(cls):
        if super()._instance == None:
            super()._instance = super().__new__(SingletonBase)
        return super()._instance

    def __init__(self):
        super()._instance = self
        self.__value  = "부모"
        print("Call Parent Init")

    def show(self):
        print(self.__value)

    def setter(self, value):
        self.__value  = value

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("자식에서 호출함")
        self.__value = "첫째"

class OtherChild(Parent):
    def __init__(self):
        super().__init__()
        print("다른 자식에서 호출함")
        self.__value = "둘째"
        self._instance.setter("22222")



c = Child()
oc = OtherChild()
c.show()
oc.show()



# class TestClass:
#     anum = 5
#     def __init__(self):
#         anum = 10

#     def Setter(self, num):
#         if self.anum < num:
#             self.anum = num
#         else:
#             print("값이 다름")

#     def cPrint(self):
#         print(self.anum)


# t = TestClass()

# while True:
#     t.Setter(int(input()))
#     t.cPrint()
