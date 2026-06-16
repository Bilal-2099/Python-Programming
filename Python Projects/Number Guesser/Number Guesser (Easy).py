# First We Import A Module Called Random
import random

# Welcome Message And Difficulty Selection Menu
print("""Welcome To The Number Guessing Game!
        I'm thinking of a number between 1 and 100.
        Please select the difficulty level:
        1. Easy (10 chances)
        2. Medium (5 chances)
        3. Hard (3 chances) """)

# Take User Input For Difficulty Level
difficulty = input("Enter the difficulty level: ")

# Dictionary That Stores Difficulty Names And Their Chances
difficulties = {
    "1": {"name": "Easy", "chances": 10},
    "2": {"name": "Medium", "chances": 5},
    "3": {"name": "Hard", "chances": 3}
}

# Check If User Entered A Valid Difficulty
if difficulty not in difficulties:
    print("Choose a valid difficulty next time.")
    quit()

# Get Difficulty Name And Chances From Dictionary
level_name = difficulties[difficulty]["name"]
chances = difficulties[difficulty]["chances"]

# Display The Selected Difficulty
print(f"Great! You have selected the {level_name} difficulty level. \n Let's start the game!")

# Generate A Random Number Between 1 And 100
random_num = random.randint(1, 100)

# Variable To Count User Attempts
guess = 0

# Start The Game Loop Until User Wins Or Runs Out Of Chances
while True:

    # Ask User To Guess A Number
    user_guess = input("Guess The Number: ")

    # Check If The Input Is A Number
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please Type a Number ")
        continue

    # Make Sure The Number Is Between 1 And 100
    if not 1 <= user_guess <= 100:
        print("Please enter a number between 1 and 100.")
        continue

    # Increase Attempt Counter After A Valid Guess
    guess += 1

    # Check If The Guess Is Correct Or Give Hints
    if user_guess == random_num:
        print(f"Congratulations! You guessed the correct number in {guess} attempts.")
        break
    elif user_guess > random_num:
        print(f"Incorrect! The number is less than {user_guess}.")
    else:
        print(f"Incorrect! The number is greater than {user_guess}")

    # Calculate And Display Remaining Attempts
    remaining = chances - guess
    print(f"Attempts remaining: {remaining}")

    # If User Uses All Chances End The Game
    if guess >= chances:
        print("You have run out of attempts. The correct number was", random_num)
        break
