def outer(x,y):
    def inner(a,b):
        print("In Innner-1 Function")

    print("In Outer Function")
    print(x + y)
    return inner

retVal = outer(10,20)
innerList = retVal(3,5)
print(retVal)
print(innerList)


        