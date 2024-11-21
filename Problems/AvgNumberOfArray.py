# Average of all the elements in the array


def average(arr):
    sum = 0
    for num in arr:
        sum += num
        
    avg = sum // len(arr)
    print(f"Average : {avg}")

arr = list(map(int,input().split()))
average(arr)