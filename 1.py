# import os
# def reverse_words_order_and_swap_cases(sentence):
#         a = sentence[::-1].split()
#         for i in a:
#             b = i[::-1]
           
#             result = b.swapcase()
#         return result

# if __name__ == '__main__':
    

#     sentence = input()

#     result = reverse_words_order_and_swap_cases(sentence)

#     print(result)
  













str = "rUns dOg"
a = str[::-1].split()
print(a)
list = []
for i in a:
    b = i[::-1]
    list.append(b.swapcase())
    
print(' '.join(list))

    
