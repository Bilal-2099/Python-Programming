import random

top_of_range = input("Type A Number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please Type Number Larger Than 0 Next Time. ")
        quit()
else:
    print("Please Type A Number Next Time. ")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess A Number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please Type A Number Next Time. ")
        continue

    if user_guess == random_number:
        print("You Got The Correct Number! ")
        break
    elif user_guess > random_number:
            print("You Were Above The Number ")
    else:
        print("You Were Below The Number. ")
    
print("You Got It In", guesses, "Guess")