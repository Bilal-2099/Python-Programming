# First With Import A Model Called Random
import random
# Now We Make Variables Of Two One Is User Means We And Second Is Computer Means Python Random Module
user_wins = 0
computer_wins = 0
# We Make Variable Named Options And Add List Of Three "Rock", "Papaer", "Scissors"
options = ["rock", "paper", "scissors"]
# From Here We Start Our Loop For The Game
while True:
# We Ask Ourselves For Our Choice
    user_input = input("Type Rock/Paper/Scissors or Q to Quit. ").lower()
# If We Want To Quit Than We Just Type Q
    if user_input == "q":
        break
# If Our Option Is Not Valid It Will Continue
    if user_input not in options:
        continue
# We Make A Variable Named Random Number And Use It As Computer Choice
    random_number = random.randint(0,2)
    # Rock:0 Paper:1 Scissors:2
# Than Computer Pick Will Be In Option List By Index
    computer_pick = options[random_number]
    print("Computer Picked", computer_pick + ".")
# We Determine The Winner By The Rules Adding It To If Else
    if user_input == "rock" and computer_pick == "scissors":
        print("You Win!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You Win!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You Win!")
        user_wins += 1

    else:
        print("You Lost")
        computer_wins += 1

# AfterWe Quit It Will Show Our Score 
print("You Won", user_wins, "Times")
print("Computer Won", computer_wins, "Times")
print("GoodBye")