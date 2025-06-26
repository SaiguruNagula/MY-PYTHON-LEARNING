# modules : a file that has code you want to reuse in other files
# modules can be imported using import keyword
# it can be built-in or user-defined

#example of built-in module
#import math 

#print(math.pi)

# user-defined module
import modulesEg as mod


print(f"The value of pi is: {mod.pi}")

c= mod.calculate_area(5)
print(f"The area of the circle with radius 5 is: {c}")


