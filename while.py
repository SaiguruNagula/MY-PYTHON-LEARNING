# while loop = will execute some code while some condition is remains true 

name = input("enter your name :")

while name == "":
    print("name should not be empty")
    name = input("enter your name :")   
print(f" entered name is {name}")

age = int(input("enter your age :"))
while age < 18:
    print("age should be greater than 18")
    age = int(input("enter your age :"))
print(f" entered age is {age}")