class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model= model

    def move(self):
        print("Vehicle move")

class car(vehicle):
    pass

class boat(vehicle):
    def move(self):
        print("Boat Move")

class plane(vehicle):
    def move(self):
        print("plane Move")


def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}





