
#       Niven Number or Not


num = int(input("Enter Number  : "))

sum  = 0
temp = num

while(num != 0):
    retVal = num % 10
    # num = num // 10
    print(retVal)
    sum = sum + retVal

if(temp % sum == 0):
    print(temp,"is a Niven Number")
else:
    print(temp, "is not a Niven Number")