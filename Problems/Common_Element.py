str1 = "Tanmayi"
str2 = "Chinmay"

s1 = set(str1)
s2 = set(str2)
print(s1)
print(s2)
common = []

for i in s1:
    for j in s2:
        if i == j:
            common.append(i)
            
print("Common Element",common)