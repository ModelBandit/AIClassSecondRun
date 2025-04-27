from pyBubble import PySort
from cBubble import cSort
import time


arrCount = 10000
start = time.time()
PySort(arrCount)
end = time.time()
print(f"{end - start: .6f} sec")

arrCount = 100000
start = time.time()
cSort(arrCount)
end = time.time()
print(f"{end - start: .6f} sec")