
# String is Pallindrome or not


def isPallindrome(name):
    return name == name[::-1]


name = input("Enter the Name : ")
ans = isPallindrome(name)

if ans:
    print("{} is pallindrome".format(name))
else:
    print("{} is not pallindrome".format(name))
