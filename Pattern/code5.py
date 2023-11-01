row = int(input("Enter Row : "))
a = 1
for i in range (1,row + 1):
    for j in range (1,row + 1):
        if(i%2 != 0):
            print("#",end=" ")
        else:
            print("$",end=" ")
    a+=1
    print()