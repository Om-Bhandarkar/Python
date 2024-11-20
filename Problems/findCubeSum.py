# Q.1 Given two Integer, Finds the sum of the cubes of all numbers in the range of n & m .


    # I/p : n = 4 and m = 9
    # O/p : 1989



def findCubeSum(start,end):

    sum = 0

    for i in range(start,end+1):

        sum += i**3
        
    print(sum)

start, end = map(int,input().split())

findCubeSum(start,end)
