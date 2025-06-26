# Static method = A method that belongs to class rather than any object of the class (instance ) 
#                 usually used for general utility functionality

# instance method = best for opertation used on the instance of the class (instance)
# Static methid = best for utility function that do not need acces to the class data

class employee:

    def __init__ (self , name , role):
        self.name= name
        self.role = role

    def get_info(self):
        print(f"employe name : {self.name}"+ "\n"+ f"role = {self.role}")

    @staticmethod
    def is_available(position):
        V_position = ["cock","cashier","manager ", "waiter", "receptinoist"]

        return position in V_position
    

print(employee.is_available('cock'))  # static method = only class is called no object is created


emp3 = employee("spongeboob","cock")
emp2 = employee("patrick","cashier")
emp1 = employee("eugine","manager")


emp1.get_info()
emp3.get_info()
emp2.get_info()


