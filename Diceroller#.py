import random 

print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
#  ● ┌ ─ ┐ │ └ ┘ 

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art={1:("┌─────────┐",
             "│         │",
             "│    ●    │",
             "│         │",
             "└─────────┘"),
          2:("┌─────────┐",
             "│ ●       │",
             "│         │",
             "│       ● │",
             "└─────────┘"),
          3:("┌─────────┐",
             "│ ●       │",
             "│    ●    │",
             "│       ● │",
             "└─────────┘"),
          4:("┌─────────┐",
             "│ ●     ● │",
             "│         │",
             "│ ●     ● │",
             "└─────────┘"),
          5:("┌─────────┐",
             "│ ●     ● │",
             "│    ●    │",
             "│ ●     ● │",
             "└─────────┘"), 
          6:("┌─────────┐",
             "│ ●     ● │",
             "│ ●     ● │",
             "│ ●     ● │",
             "└─────────┘")         }

dice=[]
total=0
is_running=True
while is_running:
   num_dice=int(input("Enter the number of dice to roll: "))
   for die in range(num_dice):
    dice.append(random.randint(1,6))
    total+=dice[die]

   for die in range(num_dice):
     for j in dice_art.get(dice[die]):
        
      print(j)
   print(f"Total: {total}")       
   continue_rolling = input("Do you want to roll again? (yes/no): ").strip().lower()  # Using strip() to remove leading/trailing spaces and lower() to handle case insensitivity
   if continue_rolling != 'yes':
       is_running = False
       print("Thanks for playing!")
    
