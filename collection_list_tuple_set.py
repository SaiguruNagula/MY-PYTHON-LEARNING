# collection = a variable that can store multiple values
# list = ordered, changeable, allows duplicates = []
# tuple = ordered, unchangeable, allows duplicates = ()
# set = unordered, unchangeable, unindexed, no duplicates = {}

fruits = ["apple", "banana", "cherry"]

print(fruits) # ['apple', 'banana', 'cherry']
print(type(fruits)) # <class 'list'>
print(fruits[0]) # apple
print(fruits[1]) # banana   
print(fruits[2]) # cherry

fruits[0] = "orange" # change the value of the first element
print(fruits) # ['orange', 'banana', 'cherry']
fruits.append("mango") # add a new element to the end of the list
print(fruits) # ['orange', 'banana', 'cherry', 'mango']
print(dir(fruits)) # to access all the methods of the list
print(help(fruits)) # to access the documentation of the list

tuple = ("apple", "banana", "cherry")
print(tuple) # ('apple', 'banana', 'cherry')    
print(type(tuple)) # <class 'tuple'>
print(tuple[0]) # apple
print(tuple[1]) # banana
print(tuple[2]) # cherry
print(dir(tuple)) # to access all the methods of the tuple
print(help(tuple)) # to access the documentation of the tuple 