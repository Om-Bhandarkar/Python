
# Try to take input to fill the array in python ( try to use array module as well as using numpy)


# 1. Array Module

import array as arr

ele = int(input("Enter the No. of Elements in array : "))

a = arr.array('i', [])


for i in range(ele):
    element = int(input(f"Enter {i} index element : "))
    a.append(element)

print(a)

for i in a:
    print(i,end=",")


# 2. Using Numpy

import numpy as np

n = int(input("Enter no. of element in numpy array : ")) 
arr =  np.empty(n,dtype = int)
for i in range(n):
    element = int(input(f"Enter {i} index element : "))
    arr[i] = element

print(arr)
