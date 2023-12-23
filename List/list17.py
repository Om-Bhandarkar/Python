def countPair(listData):
    K = int(input("Enter Number"))

    for i in range(0, n):

        for j in range(0, n):

            if K == (listData[i] + listData[j]):

                return listData[i], listData[j]


n = int(input("Enter the No. of Element : "))

listData = []

for i in range(0, n):
    ele = int(input())

    listData.append(ele)

print(listData)

ret1, ret2 = countPair(listData)

print(ret1, ret2)