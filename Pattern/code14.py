class Parent: 
    def __init__(self):
        print("In Parent Constructor")

    def ParentInfo(self):
        print("In Parent Method")


class Child(Parent):

    def __init__(self):
        print("In Child Constructor")
    
    def childInfo(self):
        print("In Child Method")


obj = Child()
obj.ParentInfo()