num = int(input("Enter Number : "))
sum = 0
while num != 0:
    x = num % 10
    sum = sum + (x**3)
    num = num // 10

