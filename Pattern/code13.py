#       A B C D       
#       A B C D       
#       A B C D       
#       A B C D

row = int(input("Enter the Number : "))

for i in range(row):

    ch = ord('A')

    for j in range(row):

        print(chr(ch),end=" ")

        ch += 1
    
    print()
        
