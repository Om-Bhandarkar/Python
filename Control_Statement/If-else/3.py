num = int(input("Enter Number : "))
sqrt = num * num
print("Square of {} is {}.".format(num,sqrt))
if sqrt % 2 ==0 :
    print(sqrt,"is Even Number.")
else :
    print(sqrt,"is Odd Number.")