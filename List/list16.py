
# list input from user

listData = []

n = int(input("Enter the Elements : "))

print("Enter {} element in list".format(n))

for i in range(0, n):

    ele = int(input())

    listData.append(ele)

print(listData)