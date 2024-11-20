def reverseArray(arr, n):

    start = 0       # 0 
    end = n-1       # 5

    while start <= end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1
    return arr



arr = list(map(int,input().split()))

n = len(arr)

result = reverseArray(arr,n)

print(", ".join(map(str, arr)))