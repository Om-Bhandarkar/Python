def PefectNumber(num):

    sum = 0

    for i in range(1,num):

        if num % i == 0:

            sum = sum + i
    print(sum)
    if num == sum:

        print(f"{num} is a Perfect Number")

    
num = int(input("Enter Number : "))

PefectNumber(num)
