import pickle

# file save
myDict = {"a":1,"b":65152,"ac":22,"asd":55,"qwe":4,}

# save only
# f = open("./pickle.pickle", "wb")
# obj1 = pickle.dump(myDict, f)
# print(obj1)

# return obj only
obj2 = pickle.dumps(myDict)
# print(obj2)

#f.close()

# file load
f = open("./pickle.pickle", "rb")
obj1 = pickle.load(f)
print(obj1)

obj3 = pickle.loads(obj2)
print(obj3)