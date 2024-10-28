def fibonacci(num,fib):

    a,b = 0,1

    for i in range(num):

        fib.append(a)

        a, b = b, a+b

    return fib



num = int(input("Enter Value :"))

fib = []

fibo_series = fibonacci(num,fib)

print(fibo_series)