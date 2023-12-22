class Company(object):

    @staticmethod
    def fun():
        print("Hello")


print("Start Main")

obj = Company()

obj.fun()  # internally call => fun(obj)

print("End Code")
