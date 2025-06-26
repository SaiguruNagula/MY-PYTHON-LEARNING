# duckTyping = another way to achieve polymorphism beside inhertiance 
#             = allows us to use objects of different classes interchangeably
#             = focuses on the methods and properties of an object rather than its class
#              = must have minimum necessary methods and properties to be considered a duck
#             = "if it looks like a duck and quacks like a duck, then it is a duck"


class Animal:
    def is_alive(self):
        return True
    
class dog(Animal):
    def speak(self):
        return "Woof!"

class cat(Animal):
    def speak(self):
        return "Meow!"
    
class car:
    is_alive = False
    def speak(self):          
        return "honk"    
    
dog = dog()
cat = cat()
car = car()

animals = [dog, cat,car]

for animal in animals:
   tin= animal.speak()
   print(tin)
    

    