
# Comprehensive Type

normalList = [num for num in range (1,11)]
print(normalList)    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(normalList)) #  <class 'list'>


sqList = [num * num for num in range (1,6)]
print(sqList)  #[1, 4, 9, 16, 25]

evenList = [num for num in range (1,11) if num % 2 == 0]
print(evenList) #[2, 4, 6, 8, 10]

