# variable scope : where a variable is accessible and visible in the code
# scope resolution : {LEGB} = local, enclosing, global, built-in


# local scope : variables defined inside a function or block
def local_scope_example():
    x = 10  # Local variable
    print(f"Local variable x: {x}")
local_scope_example()

# enclosing scope : variables defined in the outer function of a nested function
def outer_function():
    y = 20  # Enclosing variable
    def inner_function():
        print(f"Enclosing variable y: {y}")
    inner_function()
outer_function()

# global scope : variables defined at the top level of a script or module
x = 30  # Global variable
def global_scope_example():
    print(f"Global variable x: {x}")
global_scope_example()

# built-in scope : variables and functions provided by Python's built-in namespace
import builtins
def built_in_scope_example():
    print(f"Built-in function: {builtins.len([1, 2, 3])}")  # Using built-in len function
built_in_scope_example()    

# it check for the variable in the following order:
# 1. Local scope
# 2. Enclosing scope
# 3. Global scope
# 4. Built-in scope

# if there is 2 variables with the same name in different scopes, python will identify it as 2 in different scopes


# global Keyword : used to declare a variable as global inside a function
def global_keyword_example():
    global z  # Declare z as a global variable
    z = 40  # Assign a value to the global variable
    print(f"Global variable z inside function: {z}")
global_keyword_example()

print(z) # Accessing the global variable outside the function


# nonlocal Keyword : used to declare a variable as non-local inside a nested function
def nonlocal_keyword_example():
    a = 50  # Enclosing variable
    def inner_function():
        nonlocal a  # Declare a as non-local
        a = 60  # Modify the non-local variable
        print(f"Non-local variable a inside inner function: {a}")
    inner_function()
    print(f"Enclosing variable a after inner function: {a}")
nonlocal_keyword_example()
# Output:
# Non-local variable a inside inner function: 60
# Enclosing variable a after inner function: 60