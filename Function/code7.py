def factorial(N):
    fact = 1
    for i in range(1,N+1):
        fact*=1
        return fact

N = int(input("Enter value of N : "))

fact =  factorial(N)
print(fact)