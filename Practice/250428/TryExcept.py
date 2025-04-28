class TryExcept1():
    def __init__(self):
        self.num = 10
        self.string = "word"

        try:
            self.num + self.string
        except:
            print("error")
# Disassembly of __init__:
#    2           RESUME                   0

#    3           LOAD_CONST               1 (10)
#                LOAD_FAST                0 (self)
#                STORE_ATTR               0 (num)

#    4           LOAD_CONST               2 ('word')
#                LOAD_FAST                0 (self)
#                STORE_ATTR               1 (string)

#    6           NOP

#    7   L1:     LOAD_FAST                0 (self)
#                LOAD_ATTR                0 (num)
#                LOAD_FAST                0 (self)
#                LOAD_ATTR                2 (string)
#                BINARY_OP                0 (+)
#                POP_TOP
#        L2:     RETURN_CONST             0 (None)

#   --   L3:     PUSH_EXC_INFO

#    8           POP_TOP

#    9           LOAD_GLOBAL              5 (print + NULL)
#                LOAD_CONST               3 ('error')
#                CALL                     1
#                POP_TOP
#        L4:     POP_EXCEPT
#                RETURN_CONST             0 (None)

#   --   L5:     COPY                     3
#                POP_EXCEPT
#                RERAISE                  1
class TryExcept2():
    def __init__(self):
        self.num = 10
        self.string = "word"

        if self.string.isdigit() == True:
            self.num + self.string
        else:
            print("error")
#  46           RESUME                   0

#  47           LOAD_CONST               1 (10)
#               LOAD_FAST                0 (self)
#               STORE_ATTR               0 (num)

#  48           LOAD_CONST               2 ('word')
#               LOAD_FAST                0 (self)
#               STORE_ATTR               1 (string)

#  50           LOAD_FAST                0 (self)
#               LOAD_ATTR                2 (string)
#               LOAD_ATTR                5 (isdigit + NULL|self)
#               CALL                     0
#               LOAD_CONST               3 (True)
#               COMPARE_OP              88 (bool(==))
#               POP_JUMP_IF_FALSE       26 (to L1)

#  51           LOAD_FAST                0 (self)
#               LOAD_ATTR                0 (num)
#               LOAD_FAST                0 (self)
#               LOAD_ATTR                2 (string)
#               BINARY_OP                0 (+)
#               POP_TOP
#               RETURN_CONST             0 (None)

#  53   L1:     LOAD_GLOBAL              7 (print + NULL)
#               LOAD_CONST               4 ('error')
#               CALL                     1
#               POP_TOP
#               RETURN_CONST             0 (None)

# speed test
import time
from datetime import datetime

mlist = range(1, 1000000)

startTime = datetime.now()

for i in range(len(mlist)):
    if i % 1 == 0:
        mlist[i]
    mlist[0]
    
endTime = datetime.now() - startTime
print(endTime)
time.sleep(3)

startTime = datetime.now()
for i in range(len(mlist), len(mlist)+len(mlist)):
    try:
        mlist[i]
    except:
        mlist[0]

endTime = datetime.now() - startTime
print(endTime)