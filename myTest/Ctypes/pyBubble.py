temp = 0
def BubbleSort(arr):
    for i in arr:
        for j in arr:
            if i > j:
                temp = j
                j = i
                i = temp

def PySort(arrCount):
    arr = list(range(arrCount))
    arr.reverse()
    BubbleSort(arr)


