# Q.1 Find SubArray with a given sum in array. Given Interger array. Find subarrays with a Given sum in it.

#         I/P : [3,4,-7,1,3,3,1,4]
#         o/p : [3,4] [3,4,-7,1,3,3] [1,3,3] [3,3,1]

# Approach 1

# def subarry(list,target,n):
    
#     for i in range(n):
#         sum = 0
#         for j in range(i, n):

#             sum += list[j]

#             if sum == target:
#                 print(list[i:j+1])


# target = 7
# list = [3,4,-7,1,3,3,1,4]
# n = len(list)
# subarry(list,target,n)

# Approach 2

def subarray(arr,target,n):
    dict ={}
    sum = 0
    for i in range(n):
        sum += arr[i]

        if sum == target:
            print(arr[0:i+1])
        if sum - target in dict:
            print(f"Dict : {dict[sum - target]}")
            StartIndex = dict[sum - target] + 1 
            print(StartIndex)
            print(arr[StartIndex : i+1])
        dict[sum] = i
        
target = 7
list = [3,4,-7,1,3,3,1,4]
n = len(list)
subarray(list,target,n)