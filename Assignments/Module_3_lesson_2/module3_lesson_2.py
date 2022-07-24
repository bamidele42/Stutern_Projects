# The Car class

class Car:
    def __init__(self, brand, colour, model, speed):
        self.brand = brand
        self.colour = colour
        self.model = model
        self.speed = speed

    def car_brand (self):
        return f"This car is {self.brand}"

    def car_colour (self):
        return f"This car has {self.colour} colour"

    def car_model (self):
        return f"This car is {self.model}"

    def car_speed (self):
        return f"This car can cover {self.speed} per hour"

car1 = Car("volkswagen", "white", 1990, "100km")
car2 = Car("toyota", "gray", 2008, "200km")

print(car1.car_brand())
print(car2.car_brand())
print(car1.colour)
print(car2.speed)
print(car1.model)
print(car2.brand)


