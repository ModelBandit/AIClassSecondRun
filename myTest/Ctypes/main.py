from pyBubble import PySort
from cBubble import cSort
import time

import threading
threads = []

arrCount = 100000

def pSort():
    start = time.time()
    PySort(arrCount)
    end = time.time()
    print(f"python: {end - start: .6f} sec")

def ccSort():
    start = time.time()
    cSort(arrCount)
    end = time.time()
    print(f"c: {end - start: .6f} sec")

t = threading.Thread(target=pSort)
threads.append(t)
t = threading.Thread(target=ccSort)
threads.append(t)

for i in threads:
    i.start()

for i in threads:
    i.join()

print("Thread Complete")