 
print("********Reverse String using Slicing***********")

name = "Chinmay"
print("Original Name : {}".format(name)) 
print("Reverse Name : {}".format(name[::-1])) 


lst = list(name)
for i in lst:
    lst.reverse()
    