# Whether it is fibonacci or not

def isfibo(num):
    ele = 0
    while num != 0:
        a = num % 10
        ele = ele * 10 + a
        num = num // 10
    return ele

num = int(input("Enter Number : "))
x = num
if x == isfibo(num):
    print("yes")
else:
    print("no")





