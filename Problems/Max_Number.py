def Max(list):

    large = list[0]
    
    for num in list:

        if num > large :

            large = num  

    return  large 


list = [5,9,3,6,7,4,1,2]


large = Max(list)

print("Large Number",large)