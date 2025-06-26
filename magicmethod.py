# magic method = dunder method (double underscore) method __init__ , __str__ , __eq__ , __lt__ , __gt__ , __
#                the are automatically called by many of the python inbuilt operation
#                the allow developers to defin and costumize the behaviour of object

class book:
    def __init__ (self, title , author , noOfPages):    # initilize and create a object 
        self.title= title
        self.author= author
        self.noOfPages = noOfPages

    def __str__ (self):                                    # returns a string value instead of memory location while calling an object                      
        return f"{self.title} by {self.author} no of pages {self.noOfPages}"
    
    def __eq__(self, other):                           # checks for equality of 2 object 
        if not isinstance(other ,book):
          return NotImplemented
        else :
          return self.title == other.title and self.author == other.author
        
    def __lt__(self , other):                    # checks for less than of 2 object 
        if not isinstance(other ,book):
          return NotImplemented
        else :
           return self.noOfPages < other.noOfPages
        
    def __gt__(self , other):                    # checks for greater than of 2 object 
        if not isinstance(other ,book):
          return NotImplemented
        else :
           return self.noOfPages > other.noOfPages
    
    def __contains__(self , keyword):
       if keyword in self.title:
          return True
       elif keyword in self.author:
          return True
       else :
          return f'no {keyword} in the book'
        

book1 = book("nwh","stan lee", '269')    
print(book1)
book2 = book("far from home","stan ", '269') 
print(book1 == book2)
print("stan lee" in book1)




    

