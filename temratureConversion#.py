temp= float(input("Enter the temperature in  : "))
unit = input("Enter the unit (F/C) Fahrenheit and Celsius respectively : ")

if unit == 'F' or unit == 'f':
    converted = (temp-32)*5/9
    print(f"your temperature in Celsius is {converted} C")
elif unit == 'C' or unit == 'c':
    converted = (temp*9/5)+32
    print(f"your temperature in Fahrenheit is {converted} F")
else:
    print("invalid unit")