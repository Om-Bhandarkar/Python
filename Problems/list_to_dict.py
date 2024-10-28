# Write a Python Program to convert two lists into a dictionary and dictionary to tuple.

class Solution: 

    def list_to_dict(self,keys,values):

        result = dict(zip(keys,values))

        print("Dictionary ",result)

        return self.dict_to_tuple(result)

    def dict_to_tuple(self,result):
        
        print("Tuple")

        for i in result.items():
            
            print(i)

keys  = [1,2,3,4,5]

values = ['one', 'two', 'three', 'four', 'five']

obj = Solution()

obj.list_to_dict(keys,values)