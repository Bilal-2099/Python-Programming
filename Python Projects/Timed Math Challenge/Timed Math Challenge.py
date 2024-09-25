# Import the random module to generate random numbers
import random

# Import the time module to track the time taken to complete the problems
import time

# Define a list of operators to be used in the math problems
OPERATORS = ["+", "-", "*"]

# Define the minimum and maximum values for the operands
MIN_OPERAND = 3
MAX_OPERAND = 12

# Define the total number of problems to be generated
TOTAL_PROBLEMS = 10


# Define a function to generate a math problem
def generate_problem():
    # Generate two random operands within the defined range
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)

    # Choose a random operator from the list of operators
    operator = random.choice(OPERATORS)

    # Create the math expression as a string
    expr = str(left) + " " + operator + " " + str(right)

    # Evaluate the expression to get the answer
    answer = eval(expr)

    # Return the expression and the answer
    return expr, answer


# Initialize a counter for the number of wrong answers
wrong = 0

# Prompt the user to press enter to start
input("Press enter to start!")

# Print a separator line
print("----------------------")

# Record the start time
start_time = time.time()

# Loop through the total number of problems
for i in range(TOTAL_PROBLEMS):
    # Generate a problem and get the expression and answer
    expr, answer = generate_problem()

    # Loop until the user enters the correct answer
    while True:
        # Prompt the user to enter their answer
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")

        # Check if the user's answer is correct
        if guess == str(answer):
            # If correct, break out of the loop
            break
        # If incorrect, increment the wrong counter
        wrong += 1

# Record the end time
end_time = time.time()

# Calculate the total time taken
total_time = round(end_time - start_time, 2)

# Print a separator line
print("----------------------")

# Print a congratulatory message with the total time taken
print("Nice work! You finished in", total_time, "seconds!")