# quiz game 

questions = (
    "What is the capital of France?" ,
    "What is 2 + 2?",
    "What is the largest planet in our solar system?",
    "Who wrote 'Romeo and Juliet'?",
    "What is the chemical symbol for gold?",
)

options = (("A. Paris", "B. London", "C. Berlin", "D. Madrid"),
           ("A. 3", "B. 4", "C. 5", "D. 6"),
           ("A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"),
           ("A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"),
           ("A. Ag", "B. Au", "C. Pb", "D. Fe"))

answers = (
    "A",
    "B",
    "C",
    "D",
    "E",
)


gusses=[] 
score=0
question_num= 0

for question in questions:
    print("-------------------------------------")
    print(question)
    for option in options[question_num]:
     print(option)
    guess = input("Enter A, B, C, or D: ")
    guess = guess.upper()
    gusses.append(guess)
    if guess == answers[question_num]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print(f"The correct answer was {answers[question_num]}")
    print(f"Your current score is {score}/{question_num + 1}")
    print("-------------------------------------")

    question_num += 1
    

