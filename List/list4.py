
# Accessing Elements from List   1) index   2)slicing

#  Index
player = ['Rohit','Shubhman','Virat','Shreyas','KLRahul']
print(player[0]);  #Rohit
print(player[1]);  #Shubhman
print(player[2]);  #Virat
print(player[3]);  #Shreyas
print(player[4]);  #KLRahul
print(player[-3]);  #Virat
#print(player[-6]);  #IndexError


#Slicing
print(player[2::])
print(player[2:4:2])
print(player[:5:2])
print(player[-1:-5:2])

