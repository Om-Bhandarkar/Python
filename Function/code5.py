def divisible(num):

    if num % 4 == 0 and num % 5 == 0:

        print(num,"divisible by 4 and 5")

    else:

        print(num,"not divisible by 4 and 5")

val = int(input("Enter Value : "))

divisible(val)
