# Whether it is prime or not
num = int(input("Enter Number : "))
cnt = 0
for i in range(1,num+1):

    if num % i == 0:
        cnt += 1
if cnt == 2:
    print("yes")
else:
    print("no") 