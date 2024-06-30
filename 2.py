# find the length of th list and simply swap the first with (n-1)th element.

def swapElement(listData):
    n = len(listData)
    listData[0],listData[n-1] = listData[n-1],listData[0] 
    return listData

listData = [94,21,40,36,35]
print("Original Array",listData)
print("Swap Array",swapElement(listData))