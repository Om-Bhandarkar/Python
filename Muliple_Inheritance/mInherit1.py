class Parent1:
    def fun(self):
        print("In Parent1")

class Parent2:
    def fun(self):
        print("In Parent2")

class Parent3:
    def fun(self):
        print("In Parent3")

class child(Parent2,Parent1,Parent3):
    pass

obj = child()
obj.fun()