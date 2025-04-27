class MyClass:
    classVal = 15

    def InstanceCall(self, num):
        self.num = num
        print("Instance Call")
        print("self.num: {}",self.num)
        return self.num + 100
    
myClass = MyClass()
print(myClass.InstanceCall(50))

print(myClass.__class__)
print(myClass.__class__.classVal)
print(myClass.__class__.InstanceCall)