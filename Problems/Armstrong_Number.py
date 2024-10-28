

class Solution:


    def armStrong(self,num):

        sum = 0

        ele = num

        while ele != 0: 

            val = ele % 10

            sum = sum + val**3

            ele = ele // 10 

        if num == sum:
                
            print(f"{num} is a Armstrong number")

        else:

            print(f"{num} is not Armstrong Number")
    

num = int(input("Enter the Number : "))
obj = Solution()
obj.armStrong(num)