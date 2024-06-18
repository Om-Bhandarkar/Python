# Take all input as integer number and find second maximum from that.


import array

n =  int(input("Enter the number of elements in array : "))

arr = array.array('i',[])

for i in range(n):
    element = int(input())
    arr.append(element)

for i in range(n):
    if i < n-1:
        if arr[i] > arr[i+1]:
            max = arr[i]
        else:
            max = arr[i+1]
    
print(f"Maximum Number is {max}")