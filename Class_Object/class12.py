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


car1 = car("Toyota","Fortuner")
boat1 = boat("Ibiza","Touring")
plane1 = plane("Boeing","747")


for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()
    print("****************")





