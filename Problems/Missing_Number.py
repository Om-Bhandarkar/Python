def missing_Number(num):

    n = num[-1]

    total = n*(n+1)//2
    
    sum  = 0

    for i in num:

        sum = sum + i

    ans = total - sum

    return ans

num =  [1,2,4,5,6,7]

missing = missing_Number(num)

print(missing)