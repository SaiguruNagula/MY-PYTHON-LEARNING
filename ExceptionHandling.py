# Exception Handling in Python

# Example 1: Basic try-except
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# Example 2: Catching multiple exceptions
try:
    num = int("abc")
except (ValueError, TypeError):
    print("Invalid conversion!")

# Example 3: Using else and finally
try:
    result = 5 / 1
except ZeroDivisionError:
    print("Division by zero!")
else:
    print("Division successful:", result)
finally:
    print("This always runs.")

# Example 4: Raising your own exception
def check_positive(n):
    if n < 0:
        raise ValueError("Number must be positive")
    return n

try:
    check_positive(-5)
except ValueError as e:
    print("Error:", e)

# Meaning:
# - try: Code that might cause an exception.
# - except: Code that runs if an exception occurs.
# - else: Code that runs if no exception occurs.
# - finally: Code that always runs, no matter what.