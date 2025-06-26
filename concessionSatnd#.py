 # concession stand 

menu= {"popcorn": 5.00, "soda": 3.00, "candy": 2.50, "nachos": 4.50,"Samosa": 2.00}

print("_______Welcome to the concession stand!_________")
for key , value in menu.items() :
     i =  list(menu.keys()).index(key) + 1
     print(f"{i} {key:10}: ${value:.2f}")
    
print("______________________________________________")

cart = []
total = 0.0

while True:
    item = input("Enter the item or q to quit: ").lower()
    if item == 'q':
      break
    elif item in menu:
        cart.append(item)
        total += menu[item]
        print(f"{item} added to cart. Total: ${total:.2f}")
    else:
        print("Item not found. Please try again.")
print("Your cart:")
for item in cart:
    print(f"- {item}")
print(f"Total amount due: ${total:.2f}")
# print("Thank you for shopping with us!")
    