# list compression : compact way to create a list using a single line of code
# list compression = [expression for value in iterable if condition]


# normal list
double=[]
for x in range(10):
    double.append(x*2)

print(double)

# list comprehension
double_comp = [x * 2 for x in range(10)] # no condition applied yet 

print(double_comp)

fruits=['apple','banana','mango','watermelon','pineapple']
fruits=[x.upper() for x in fruits ]
print(fruits)

# list comprehension with condition
numbers=[1,2,-4,5,8,7,-3,-7, 9]

numbers_positive =[x for x in numbers if  x>=0] # only positive numbers condition applied

print(numbers_positive)
