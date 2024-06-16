class Info:
    # Class Variable
    collegeName = "JSPM NTC"
    def __init__(self,name,percentage):
        # Instance Variable
        self.name = name
        self.percentage = percentage
    def display(self):
        print("My Name is {} and My age is {}".format(self.name,self.percentage))

obj1 = Info("Chinmay",8.0)
obj2 = Info("Om",7.57)
obj3 = Info("Namrata",8.80)

# for Object 1
print(obj1.name)
obj1.display()

# for Object 2
print(obj2.name)
obj2.display()

# for Object 3
print(obj3.name)
obj3.display()

# for class Variable

print(obj1.collegeName)
print(obj2.collegeName)
print(obj3.collegeName)