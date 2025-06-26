#membership operator # membership operator is used to check if a value is present in a sequence (string, list, tuple, etc.)
# membership operator = in, not in

word = 'APPLE'
input_letter = input("enter the letter to check: ").upper()


if input_letter in word:                # in is a membership operator
        print(f"{input_letter} is found")
else:
        print(f"{input_letter} is not found")

if input_letter not in word:                # not in is a membership operator
        print(f"{input_letter} is not found")
else:
        print(f"{input_letter} is  found")