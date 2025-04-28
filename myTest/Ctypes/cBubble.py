import ctypes
from array import array

# 자리 이동시 파일패스를 확인할 것
def cSort(arrCount):
    lib = ctypes.cdll.LoadLibrary('C:\Workspace\AIClassSecondRun\myTest\Ctypes\CtypesTest.dll')
    #or CDLL(adress)

    num = list(range(arrCount))
    num = array('I', num)
    num = (ctypes.c_int * arrCount).from_buffer(num)

    lib.BubbleSort.restype = ctypes.c_char_p
    lib.MyFunc()

    cp = lib.BubbleSort(num, arrCount)

    print('\n',cp)