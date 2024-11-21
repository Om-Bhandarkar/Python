
def arraySum(arr):

    sum = 0
    for num in arr:
        sum += num
    return sum
        

arr = list(map(int,input().split()))
result = arraySum(arr)
print(result)
