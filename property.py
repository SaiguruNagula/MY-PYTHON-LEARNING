# property = decorator used to defin a method as property ( it ca be used as a attritbute)
#            Benefit : ADD additional logic when read , write , and delete attribute
#            gives u getter , setter, deleter method

class rectangle:
    def __init__(self, width , height):
        self._width = width               # prefix with _ to make it private
        self._height = height

    @property      # getter method
    def width(self):
        return f"{self._width:.2f}cm"
    @property
    def height(self):
        return f"{self._height:.2f}cm"
    
    @width.setter
    def width(self, new_width):
      if new_width <0 :
         print(f"must be greater than zero")
      else :
          self._width = new_width
    
    @height.setter
    def height(self, new_height):
      if new_height <0 :
         print(f"must be greater than zero")
      else :
          self._height = new_height

# deleter can also used :
# del shape.width
#del shape.height       but we wont use these

    @width.deleter
    def width(self):
       del self._width
       print("width has been deleted")

    @height.deleter
    def height(self):
       del self._height
       print("width has been deleted")


shape = rectangle(3,4)

#print(shape.width)
#print(shape.height)

# after setter
shape.width = -6

print(shape.width)
print(shape.height)

# after deleter

del shape.width

