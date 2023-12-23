def fun():
    print("Start fun")

    yield 10

    yield 20

    yield 30

    print("End fun")


ret = fun()

print(type(ret))

print(type(fun))

for val in ret:
    print(val)
