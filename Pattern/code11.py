#           1   4  9         
#           16  25 36      
#           49  64 81


row = int(input("Enter Row : "))

a = 1

for i in range(1,row+1):

    for j in range(1,row+1):
        
        print(a**2,end=" ")

        a+=1

    print()

