# multilevel inheritance = allow class to inherit properties and methods from another class
#                          A(B,c) = 


# multiple inheritance = allow class to inherit properties and methods from multiple classes
#                          c(b) <- b(a) <- a()
class Animal:
    def __init__(self, name):
        self.name = name
        

    def is_alive(self):
        print(f"{self.name} is alive.")

    def is_eating(self):
        print(f"{self.name} is eating.")

    def is_sleeping(self):
        print(f"{self.name} is sleeping.")
    def is_alive(self):
        print("This animal is alive.")
    def is_eating(self):
        print("This animal is eating.")
    


class prey(Animal):
    # prey is a subclass of Animal
    # prey inherits properties and methods from Animal
    # prey can have its own properties and methods
    # prey can override properties and methods from Animal
   def is_pray(self):
         print(f"{self.name} is a prey animal.")

class predator(Animal):
    # predator is a subclass of Animal
    # predator inherits properties and methods from Animal
    # predator can have its own properties and methods
    # predator can override properties and methods from Animal
   def is_predator(self):
         print(f"{self.name} is a predator animal.")

class rabbit(prey):
 pass

class fox(predator):
    pass

class fish(prey, predator):
  pass


rabbit = rabbit()
fox = fox()
fish = fish()

rabbit.is_pray()  # Output: This is a prey animal.
fox.is_predator()  # Output: This is a predator animal.
fish.is_pray()  # Output: This is a prey animal.
fish.is_predator()  # Output: This is a predator animal.
# fish.is_pray() and fish.is_predator() demonstrate multiple inheritance, where fish inherits from both prey and predator classes. 


fish.is_alive()  # Output: This animal is alive.
fish.is_eating()  # Output: This animal is eating.
# fish can access methods from both prey and predator classes, demonstrating the power of multiple inheritance.

