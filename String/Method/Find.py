#   Find() => return Type int 
#   rfind() => We find last string index

str1 = input("Enter String : ")
str2 = input("Enter Sub String : ")

str3 = str1.rfind(str2)      # We find default first string index

if str3 == -1:
    print(str2 + " Not Found")
else:
    print(str2 + " Found at Index {}".format(str3))



