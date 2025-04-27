import ctypes
from array import array

def cSort(arrCount):
    lib = ctypes.cdll.LoadLibrary('./CtypesTest.dll')
    #or CDLL(adress)

    num = list(range(arrCount))
    num = array('I', num)
    num = (ctypes.c_int * arrCount).from_buffer(num)

    lib.BubbleSort.restype = ctypes.c_char_p
    lib.MyFunc()

    cp = lib.BubbleSort(num, arrCount)

    print('\n',cp)