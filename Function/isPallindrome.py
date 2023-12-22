def checkPalindrome(num):
    reverseNum = 0
    num2 = num

    while (num2 > 0):
        lastDigit = num2 % 10
        reverseNum = reverseNum * 10 + lastDigit
        num2 = num2 // 10

    if (num == reverseNum):
        return 1

    else:
        return 0
num = int(input("Enter Number : "))

if(checkPalindrome(num)):

    print("{} is Pallindrome".format(num))

else:

    print("{} is not Pallindrome".format(num))