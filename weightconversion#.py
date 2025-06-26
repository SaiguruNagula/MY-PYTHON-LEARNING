# weight conversion 

weight= float(input("Enter your weight : "))
unit=input("enter the unit (k/lbs) kilogram and pounds respectively :")

if unit == 'k':
    converted = weight*2.20462
    print(f"your weight in pounds is {converted} lbs")
elif unit == 'pounds':
    converted = weight/2.20462
    print(f"your weight in kgs is {converted} kg")

else :
    print("invalid unit")
