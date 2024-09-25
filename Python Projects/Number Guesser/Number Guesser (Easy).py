# First With Import A Model Called Random
import random
# Type Number
top_of_range = input("Type A Number: ")
# In This If The Variable Is aceept If Larger Than 0 If Not Then There Is Else And Nested If
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please Type Number Larger Than 0 Next Time. ")
        quit()
else:
    print("Please Type A Number Next Time. ")
    quit()
# Now We Take Our Random Module In Use By Randint In It We Enter To Value Start And Stop In Start We Add 0 And In Stop We Add top_of_range
random_number = random.randint(0, top_of_range)
# We Add Variable Named Guesses To Count Our guesses
guesses = 0
# From Here We Start A Loop That Continues Until The We Guess The Correct Number
while True:
# No Matter If Our Guess Is Wrong Or Right It Will Add A Value In It
    guesses += 1
# Enter Your Guess
    user_guess = input("Guess A Number: ")
# Confirm It's A Number
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please Type A Number Next Time. ")
        continue
# If The Number Is Correct Than Tell Us Or Give Us Hints
    if user_guess == random_number:
        print("You Got The Correct Number! ")
        break
    elif user_guess > random_number:
            print("You Were Above The Number ")
    else:
        print("You Were Below The Number. ")
    
# After Guessing The Correct Number It Tells Us And Mentioned Our Guesses   
print("You Got It In", guesses, "Guess")