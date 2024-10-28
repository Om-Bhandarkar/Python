def Min(list):

    small = list[0]
    
    for num in list:

        if num < small :

            small = num  

    return  small 

    
list = [5,9,3,6,7,4,1,2]


small = Min(list)

print("Small Number : ",small)