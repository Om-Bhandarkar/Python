# Rotate array by K elements


arr = list(map(int,input().split()))
n = len(arr)

k = int(input("Enter Element : "))

temp = []

for i in range(n):

    var = arr[(i+k) % n]
    temp.append(var)

print(temp)