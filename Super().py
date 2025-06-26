#super(): used in child to call methods from parent class
# super() is a built-in function in Python that returns a temporary object of the superclass (parent class) that allows you to call its methods.

class shape:
 def __init__ (self , color, is_filled):
      self.color = color
      self.is_filled = is_filled


class circle:
 def __init__(self,color,is_filled, radius):
   super().__init__(color, is_filled)
   self.radius = radius


class square:
    def __init__(self, color, is_filled, side_length):
     super().__init__(color, is_filled)
     self.side_length = side_length

class rectangle:
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height


circle - circle("red", True, 5)
square = square("blue", False, 4)
rectangle = rectangle("green", True, 3, 6)
print(f"Circle: Color={circle.color}, Filled={circle.is_filled}, Radius={circle.radius}")
print(f"Square: Color={square.color}, Filled={square.is_filled}, Side Length={square.side_length}")
print(f"Rectangle: Color={rectangle.color}, Filled={rectangle.is_filled}, Width={rectangle.width}, Height={rectangle.height}")
# Output:
# Circle: Color=red, Filled=True, Radius=5
# Square: Color=blue, Filled=False, Side Length=4
# Rectangle: Color=green, Filled=True, Width=3, Height=6


