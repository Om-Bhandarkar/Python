class Parent :
    def __init__(self):
        print("In Parent constructor")
    def parentInfo(self):
        print("In Parent Funtion")

class child(Parent) :
    pass

obj = child()
obj.parentInfo()
 