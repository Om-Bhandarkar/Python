row = int(input("Enter Row : "))
a = 1
for i in range (1,row + 1):
    for j in range (1,row + 1):
        print(a,end=" ")
        a+=2
    a-=4
    print()