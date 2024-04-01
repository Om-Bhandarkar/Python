def swapList(list):
    list[0], list[-1] = list[-1], list[0]
    return  list


list = [10,12,14,15,16]

print("Original List : ",list)
print("Swapped List : ",swapList(list))