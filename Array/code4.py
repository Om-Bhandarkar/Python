# Take all input as integer number and find second maximum from that.
n = int(input("Enter Number of elements in array: "))
arr = []
for i in range(n):
    ele = int(input("Enter number: "))
    arr.append(ele)



if arr[0] > arr[1]:
    maxNum = arr[0]
else:
    maxNum = arr[1]
for i in range(2, n):
    if arr[i] > maxNum:
        maxNum = arr[i]

print("Maximum Number is:", maxNum)
