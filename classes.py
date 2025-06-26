from Car import cars

class student():

    class_jo_year = 2024  # class variable
    no_of_students = 0  # class variable to

    def __init__(self, name, roll_no, age):  # constructor
        self.name = name                      # instance variable
        self.roll_no = roll_no
        self.age = age
        student.no_of_students += 1
        print(f"New student added: {self.name}, Total students: {student.no_of_students}")


    def study(self):  # method
        print(f"{self.name} is studying.")

    def take_exam(self):
        print(f"{self.name} is taking an exam.")
stidemt1 = student("Alice", 101, 20)
stidemt2 = student("Bob", 102, 22)
stidemt3 = student("Charlie", 103, 21)

print(f"Total number of students: {student.no_of_students}")

 
car1 = cars("ford", 'mustang',('mh',48 , 1002), True)
car2 = cars("BMW", 'WERRON',('mh',48 , 1003), True)

print(car1.name, end='\t')
print(car1.model,end='\t')
print(car1.number,end='\t')
print(car1.for_sale)


car1.drive()
car2.drive()

print(car1.class_jo_year)
