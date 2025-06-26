# inheritance = allow class to inherit properties and methods from another class  
#               helps to reduce code duplication and helps with reusability and readability
#               eg Child(Parent):   

class Animal:
    def __init__ (Self, name , spicies):
        Self.name = name
        Self.spicies = spicies

    def is_alive(Self):
        print(f"{Self.name} is alive.")

    def is_eating(Self):
        print(f"{Self.name} is eating.")   

    def is_sleeping(Self):
        print(f"{Self.name} is sleeping.")

class Dog(Animal):
    def sound(Self):
        print(f"{Self.name} barks.")

class cat(Animal):
    pass

dog = Dog("Buddy", "Golden Retriever")
cat = Animal("Whiskers", "Siamese")
print(f"Dog Name: {dog.name}, Species: {dog.spicies}")

print(dog.is_alive())

