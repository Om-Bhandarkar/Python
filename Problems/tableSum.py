
def tableSum(num):

    table = 0
    sum = 0
    for i in range(1,11):
        table = num * i
        sum += table

    print(sum)

num = int(input())

tableSum(num)