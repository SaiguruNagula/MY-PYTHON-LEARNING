# format specifier = {value Flag} format a value based on what flag are inserted

value1= 3.14159
value2= -2.7856
value3= 18.90

print(f"Value1 is {value1:.2f}") # 2 decimal places
print(f"Value2 is {value2:.3f}") # 3 decimal places
print(f"Value3 is {value3:.1f}") # 1 decimal place
print(f"Value1 is {value1:.0f}") # 0 decimal places
print(f"Value1 is {value1:.2e}") # scientific notation
print(f"Value1 is {value1:.2E}") # scientific notation with E
print(f"Value1 is {value1:.2%}") # percentage
print(f"Value1 is {value1:.2%}") # percentage with 2 decimal places

print(f'value is {value3:>10}') # 4 digits with leading zeros