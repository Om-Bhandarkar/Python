# reverse array


n = int(input("Enter Size : "))
arr = []
for i in range(n):
   ele = int(input())
   arr.append(ele)
print(f"Original Array : {arr}")
print()
print(f"Reverse Array : {arr[::-1]}")
print(arr)

