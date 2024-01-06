def swapInteger(list,pos1,pos2):

    list[pos1],list[pos2] = list[pos2],list[1]

    return list


pos1 = int(input("Enter POS 1 : "))
pos2 = int(input("Enter POS 2 : "))

list = [10,20,30,40,50]

retList = swapInteger(list,pos1-1,pos2-1)

print(retList)





















