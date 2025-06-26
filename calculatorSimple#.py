print("enter the number for operation:")
a = int(input())
print("enter the number for operation:")
b = int(input())
print("enter the operation :")
print(" + for addition, - for subtraction, * for multiplication, / for division, % for modulus, ** for exponentiation, // for floor division")
operation = input()

if operation == '+':
    print(a+b)
elif operation == '-':
    print(a-b)
elif operation == '*':
    print(a*b)
elif operation == '/':
    print(a/b)
elif operation == '%':
    print(a%b)
elif operation == '**': 
    print(a**b)
elif operation == '//':
    print(a//b)
else:
    print("invalid operation")