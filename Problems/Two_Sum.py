def twoSum(arr,target):
    list = []
    arr.sort()

    left = 0
    
    right = len(arr) - 1

    while left <= right:

        if arr[left] + arr[right] > target:

            right = right - 1

        elif arr[left] + arr[right] < target:

            left = left + 1

        elif arr[left] + arr[right] == target:

            # print("Values of pair are",arr[left],"&",arr[right])
            list.append(arr[left])
            list.append(arr[right])
            right = right - 1

            left = left + 1
        
    return list
    

arr = [1,4,45,6,10,8]

target = 16

ans = twoSum(arr,target)
print(ans)
