row=int(input("Enter row: "))
for i in range(row):
    n=i+1;
    num=(n*(n+1))//2
    for j in range(i+1):
        print(num,end=" ");
        num+=1;
    print()