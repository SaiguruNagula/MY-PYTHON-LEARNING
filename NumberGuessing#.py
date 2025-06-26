import random

lowest_number = 1
highest_number = 100
answer= random.randint(lowest_number, highest_number)

gusses =0
is_running=True

while is_running:
    guess= input(f"enter the no between {lowest_number} and {highest_number}  ")

    if guess.isdigit():
        guess = int(guess)
        gusses +=1
        if guess<lowest_number or guess>highest_number:
            print(f"please enter a valid number")
            print(f"enter th number between {lowest_number} and {highest_number}")
        elif guess< answer:
            print("too low")    
        elif guess> answer:
            print("too high")
        elif guess == answer:
             print(f"you gussed the correct number : {answer} ")
             print(f"you gussed the number in {gusses} attempts")
             print("game over")
             is_running = False
    

    else:
        print("please enter a valid number")
        print(f"enter th number between {lowest_number} and {highest_number}")
           
        