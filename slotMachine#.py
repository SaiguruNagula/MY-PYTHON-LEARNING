#slot machine program
import random
def slot_machine():
    print("Welcome to the Slot Machine!")
    print("You have 100 coins to start with.")
    
    coins = 100
    while coins > 0:
        print(f"\nYou have {coins} coins.")
        bet = int(input("Enter your bet (1-10 coins): "))
        
        if bet < 1 or bet > 10:
            print("Invalid bet. Please enter a value between 1 and 10.")
            continue
        
        if bet > coins:
            print("You don't have enough coins for that bet.")
            continue
        
        # Simulate the slot machine
        symbols = ['🍒', '🍋', '🍊', '🍉', '⭐']
        result = [random.choice(symbols) for _ in range(3)]
        
        print("Spinning...")
        print(" | ".join(result))
        
        if result[0] == result[1] == result[2]:
            winnings = bet * 10
            coins += winnings
            print(f"Congratulations! You won {winnings} coins!")
        else:
            coins -= bet
            print(f"You lost {bet} coins.")
        
        if coins <= 0:
            print("You have run out of coins. Game over!")
            break
    
    print("Thank you for playing the Slot Machine!")