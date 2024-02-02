def add(x):
    def inner(y):
        return x*y
    return inner
if __name__ == '__main__':
    sum = add(3)
    result = sum(7)
    print(result)