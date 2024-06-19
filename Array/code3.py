# Take inputs to array as characters and then print only vowels in first line and consonant in other line

# import array
# name = input("Enter Name : ")
# v = "aeiouAEIOU"

# vowel = array.array('u',[])
# consonant = array.array('u',[])
# for i in name:
#     if i in v:
#         vowel.append(i)
#     if i not in v:
#         consonant.append(i)

# print(vowel)
# print(consonant)

name = input("Enter Name : ")
v = "aeiouAEIOU"

vowel = []
consonant = []
for i in name:
    if i in v:
        vowel.append(i)
    if i not in v:
        consonant.append(i)

for i in vowel:
    print(i, end=" ")

print()

for i in consonant:
    print(i, end=" ")




