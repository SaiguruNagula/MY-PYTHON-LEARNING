# matchcase = alternative to many elif statements
#             execiutes when match case is found 
#             benefits : easy to read and write and clean code

def week_of_days(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day number, please enter a number between 1 and 7."

print(week_of_days(1))  # Output: Monday
print(week_of_days(5))  # Output: Friday    
print(week_of_days(8))  # Output: Invalid day number, please enter a number between 1 and 7.


def weekend(day):
    match day:
        case 'sunday'  | 'saturday':  # Matches both Saturday and Sunday
            return "It's the weekend!"
        case _:
            return "It's a weekday."