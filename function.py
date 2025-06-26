#function : a block of resuable code 
#           place() after to call the function name to invoke it 

# example: 

def happy_birthday() :
    print('''happy birth day to you , 
          you are now old , 
          may good bless you! ''')

# fn call

happy_birthday()       

# return 
# function can return a value using the return keyword
def add(a,b):
    return a + b

add(5,10)
print(add(5,10))  # Output: 15 

# function with parameters
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")  # Output: Hello, Alice!

# function with default parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")
    
greet()  # Output: Hello, Guest!
greet("Bob")  # Output: Hello, Bob!

# function with positional arguments 
def full_name(fname , lname):
    fname.capatlize()
    lname.capitalize()
    return f"{fname} {lname}"
print(full_name("john", "doe"))  # Output: John Doe

# function with keyword arguments

def stu_name(fname , lname, age, id ):
    return f"Name: {fname} {lname}, Age: {age}, ID: {id}"
print(stu_name(id=123, fname="Alice", lname="Smith", age=20))  # Output: Name: Alice Smith, Age: 20, ID: 123

# function with variable-length arguments
def add_numbers(*args):
    return sum(args)
print(add_numbers(1, 2, 3))  # Output: 6
print(add_numbers(1, 2, 3, 4, 5))  # Output: 15  tuple type


# function with keyword variable-length arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=30, city="New York")
# Output:   
# name: Alice
# age: 30       dictionary type