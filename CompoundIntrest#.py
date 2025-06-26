# python compound intrest calculator

principal = 0
rate = 0
time = 0


while principal <= 0:
    principal = float(input("Enter the principal amount (greater than 0): "))
    if principal <= 0:
        print("Principal amount should be greater than 0. Please try again.")

while rate <= 0:
    rate = float(input("Enter the rate of interest (greater than 0): "))
    if rate <= 0:
        print("Rate of interest should be greater than 0. Please try again.")

while time <= 0:
    time = float(input("Enter the time in years (greater than 0): "))
    if time <= 0:
        print("Time should be greater than 0. Please try again.")

# Calculate compound interest
total  = principal * pow((1 + rate / 100), time) 
print(f"total amount after {time} years is: {total:.2f}")