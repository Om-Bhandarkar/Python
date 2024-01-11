def primeNumber(num):
    count = 0
    while num != 0:
        if num % 2 == 0 :
            count+=1
        num =- 1
    if count == 2:
        print("Prime")
    else:
        print("Not Prime")
        
num = int(input("Enter the Number : "))

primeNumber(num)





