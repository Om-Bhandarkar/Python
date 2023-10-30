num = 1
row = 5

def fn(num):
    sum=0
    temp1 = num
    while (temp1 != 0):
        retVal = temp1 % 10
        temp1 = temp1 // 10
        sum = sum + retVal

    if (num % sum == 0):
        return num
    else:
        return 0


var = 1
for i in range(1,row+1):
    for j in range(1,row+1):
        print(fn(var), end=" ")
        var+=1

    print()




