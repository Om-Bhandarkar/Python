# Find the smallest element in an array

def getMin(arr):
    minElement = float('inf')
    
    for i in range(len(arr)):
        minElement = max(minElement,arr[i])
        print(f"minElement: {minElement}")
    return minElement
    
arr = list(map(int,input().split()))
res = getMin(arr)
print(f"Smallest Element : {res}")

