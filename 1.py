str = "kashsak"
start, end = 0, len(str)-1

while start <= end:
    if str[start] == str[end] :
        start+=1
        end-=1
    else:
        flag = 1
        break
    flag = 0

if flag == 0:
    print("Pallindrome String")
else:
    print("Not Pallindrome String")

