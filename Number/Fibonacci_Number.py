# Fibonacci Series

num = int(input("Enter Number : "))

a = 0
b = 1
sum  = 0

for i in range(num):
    print(sum,end=" ")
    sum = a + b
    b = a
    a = sum


