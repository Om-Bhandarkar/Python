#Reverse integer

n  =  int(input("Enter size of array : "))
intArray = []
for i in range(n):
    ele = int(input("Enter Element : "))
    intArray.append(ele)
print(intArray) 

for i in range(n):
    if intArray[i] % 2 == 0:
        print(intArray[i],end=" ")