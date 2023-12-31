#           A B C         
#           D E F         
#           G H I  


row = int(input("Enter the row : "))

ch = ord("A")

for i in range(row):

    for j in range(row):

        print(chr(ch),end=" ")

        ch += 1
    
    print()
