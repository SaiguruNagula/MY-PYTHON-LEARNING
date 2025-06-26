import random

option=("rock", "paper", "scissors")
print("Welcome to Rock, Paper, Scissors!")
is_running = True

while is_running :

   computer_points=0
   user_points=0

   while computer_points < 5 and user_points < 5:
     computer_choice= random.choice(option)
     user_choice= input("Enter your choice (rock, paper, scissors)  ").lower()
     if user_choice not in option :
        print(f"invalid choice from {option}")
       
     elif user_choice == computer_choice:
        print(f"computer choice is {computer_choice}")
        print("It's a tie!")   

     elif user_choice == "rock" and computer_choice == "scissors":
        print(f"computer choice is {computer_choice}")
        print("You win! Rock crushes scissors.")
        user_points += 1
        print(f"you points = {user_points} and computer points = {computer_points}")

     elif user_choice == "paper" and computer_choice == "rock":
        print(f"computer choice is {computer_choice}")
        print("You win! Paper covers rock.")
        user_points += 1
        print(f"you points = {user_points} and computer points = {computer_points}")

     elif user_choice == "scissors" and computer_choice == "paper":
        print(f"computer choice is {computer_choice}")
        print("You win! Scissors cut paper.")
        user_points += 1
        print(f"you points = {user_points} and computer points = {computer_points}")

     else:
        print(f"computer choice is {computer_choice}")
        print("You lose!")
        computer_points += 1         
        print(f"you points = {user_points} and computer points = {computer_points}")

   print(f"your point {user_points} and computer points {computer_points}")
   if computer_points > user_points :
       print("better luck next time")
   else :
       print("congrats you won")
   print("______________________________________________________________")    
   
   st= input("DO u want to try again press (y/n) ").lower()
   if st != "y" :
      print("Thanks for playing ")
      is_running=False    