with open("./ZoomNum.txt", 'r') as f:
    data = f.read()
    print(data)

fp = open("./ZoomNum.txt")
print(fp)
print(id(fp))
print(type(fp), end="\n\n")

fp.close()
