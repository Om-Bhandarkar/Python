def isStrong(num):
    
    num2 = num 

    while(num2 > 0):

        val = num2 % 10

        fact = 1

        for i in range(1,val+1):

            fact = fact * i

        sum = 0

        sum = sum + fact

        print(sum)

        num2 = num2 // 10
        

num = int(input("Enter the Number : "))

isStrong(num)





