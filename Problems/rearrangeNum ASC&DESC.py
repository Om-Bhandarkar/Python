# Rearrange array in increasing-decreasing order


def rearrange(arr,n):
    arr.sort()
    for i in range(n // 2):
        print(arr[i],end=" ")

    for i in range(n-1,n//2 - 1,-1):
        print(arr[i],end=" ")
    
    

arr = list(map(int,input().split()))
n = len(arr)
rearrange(arr,n)



