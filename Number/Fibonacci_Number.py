# Fibonacci Series (General)

num = int(input("Enter Number : "))

a = 0
b = 1
sum  = 0

for i in range(num):
    print(sum,end=" ")
    sum = a + b
    b = a
    a = sum

# Using Function

def fibonacci_with_list(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

n = 10
result = fibonacci_with_list(n)
print(f"Fibonacci series with {n} elements:", result)
        


