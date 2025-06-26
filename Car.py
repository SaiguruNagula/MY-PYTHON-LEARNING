class cars():
    class_jo_year = 2024 # class variable

    def __init__(self, name , model , number, for_sale):  # constructor   , while always be initated as object is created
        self.name = name                      # instance variable
        self.model = model                       
        self.number = number
        self.for_sale = for_sale
    def drive(self):                                            # method
        print(f"u are driving {self.name} {self.model}")


    def stop(self):
        print(f"u have stopped {self.name} {self.model}")          

          