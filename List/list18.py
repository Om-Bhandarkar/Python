def printList(x,listData):
    
    for i in range(x):
        listData.append(i*i)
    
    print(listData)

printList(3,[1,2])