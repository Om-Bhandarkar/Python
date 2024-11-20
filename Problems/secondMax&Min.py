def getSecondMax(arr):
    max, secondMax = float('-inf'), float('-inf')
    for num in arr:
        if len(arr) == 1:
            return -1
        if num > max:
            secondMax = max
            max = num
        elif max > num > secondMax:
            secondMax = num
    return secondMax if secondMax != float('-inf') else -1


def getSecondMin(arr):
    min, secondMin = float('inf'), float('inf')
    for num in arr:
        if len(arr) == 1:
            return -1
        if num < min:
            secondMin = min
            min = num
        elif num < secondMin and num > min:
            secondMin = num
    return secondMin if secondMin != float('inf') else -1

arr = list(map(int,input().split()))

secondMax = getSecondMax(arr)
print(f"Second Maximum : {secondMax}")

secondMin = getSecondMin(arr)
print(f"Second Minimum : {secondMin}")
