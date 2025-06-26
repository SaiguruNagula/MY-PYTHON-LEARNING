# polymorphism = greek word meaning "many forms" or faces
# polymorphism is a concept in OOP that allows objects of different classes to be treated as objects of a common superclass

from abc import ABC, abstractmethod

class shape :
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class square(shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2
class rectangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class pizza(circle) :
    def __init__(self , toppings , radius):
        self.toppings = toppings
        self.radius = radius
    

# Example usage

shapes = [circle(5), square(4), rectangle(3, 6), pizza("pepperoni", 3)]

for shape in shapes:
    print(f"Area: {shape.area()}.cm^2")  # Calls the area method of each shape object4
# Output:
# Area: 78.5
# Area: 16
# Area: 18
# Area: 50.24
