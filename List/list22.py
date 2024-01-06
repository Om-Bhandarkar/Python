
# write a Python program to swap first and last element of the list.

def swap(newList):
    size = len(newList)

    temp = newList[0]
    newList[0] = newList[-1]
    newList[-1] = temp

    return newList



listData = swap([10,20,30,40,50])

print(listData)




'''
def swap(list):

    a,*b,c = list
    list = [c,*b,a]
    return list


retVal = swap([1,2,3,4,6,7])
print(retVal)

'''



'''
def swap(newList):
    
    newList[0],newList[-1] = newList[-1],newList[0]

    return newList


retList = swap([10,20,30,40,50])
print(retList)
'''