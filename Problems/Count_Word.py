def freq_word(str):

    li = str.split()

    dict = {}

    for i in li:

        if i not in dict.keys():

            dict[i] = 0
            
            print(dict)

        dict[i] = dict[i] + 1

    print(dict)


str = input("Enter a string :")
freq_word(str)