# Take all input as integer number and find second maximum from that.

n = int (input("Enter Number of element in array: "))
arr = []
for i in range(n):
    ele = int(input("Enter number : "))
    arr.append(ele)

print(arr)

for i in arr:
    arr.sort()

print("Second Maximum Number is : ",arr[-2])