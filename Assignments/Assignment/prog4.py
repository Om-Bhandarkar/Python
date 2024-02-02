def myParentFunction():
    def myIndex(str):
        index = 0
        while index < len(str):
            if str[index] == 'A':
                break
            index += 1
        return index

    def myPalindrome(str):
        str = str.lower()
        str = ''.join(e for e in str if e.isalnum())
        return str == str[::-1]

    print("1. Find Index")
    print("2. Check Palindrome")
    print("Enter the number of the operation you want to perform:")
    operation = int(input())

    if operation == 1:
        user_input = input("Enter a string: ")
        result = myIndex(user_input)
        print("The index of the first occurrence of 'A' is: ", result)

    elif operation == 2:
        user_input = input("Enter a string: ")
        result = myPalindrome(user_input)
        if result:
            print("The string is a palindrome.")
        else:
            print("The string is not a palindrome.")
            
    else:
        print("Invalid operation number.")

myParentFunction()