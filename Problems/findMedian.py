
# Find Median of the given Array

def getMedian(arr):
    arr.sort()
    if len(arr) % 2 == 0:
        ind1 = (len(arr) // 2) - 1
        ind2 = (len(arr) // 2)
        return (arr[ind1]+ arr[ind2]) / 2
    return arr[len(arr)//2]

arr = list(map(int,input().split()))
retVal = getMedian(arr)
print(retVal)