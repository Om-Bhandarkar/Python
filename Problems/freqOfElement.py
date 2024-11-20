def countFreq(arr,n):
    x = [False] * n
    
    for i in range(n):
        if x[i] == True:
            continue
        count = 1
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                x[j] = True
                count+=1
        
        print(arr[i],count)


arr = list(map(int,input().split()))
n= len(arr)

countFreq(arr,n)