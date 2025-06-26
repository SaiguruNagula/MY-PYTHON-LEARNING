import random

#print(help(random))

number = random.randint(1,100)  # intiger
number2 = random.random()  # float
number3 = random.uniform(1,5)  # float
cards=['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


print(number)
print(number2)
print(number3)

options = ["rock", "paper", "scissors"]
option = random.choice(options)
print(option)


# shuffle the cards
random.shuffle(cards)
print(cards)  # shuffled cards