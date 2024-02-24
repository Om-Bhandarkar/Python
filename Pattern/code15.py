#       A 
#       B C 
#       D E F         
#       G H I J       
#       K L M N O 

num = int(input("Enter the Row : "))
x = ord('A')   # Turn char into the int
for i in range(1,num+1):
    for j in range(1,i+1):
        print(chr(x),end=" ")
        x += 1
    print("")