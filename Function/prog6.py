def divisible(x):

    if(x%4==0 and x%5==0):

        print(x,"is divisible by 4 & 5")

    else:

        print(x,"is not divisible by 4 & 5")

num = int(input("Enter the Number : "))

divisible(num)
