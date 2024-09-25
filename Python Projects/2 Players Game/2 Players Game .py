import random

# Define a function to simulate a dice roll
def roll():
    # Set the minimum and maximum values for the dice roll
    min_value = 1
    max_value = 6
    # Generate a random integer between min_value and max_value
    roll = random.randint(min_value, max_value)
    # Return the result of the dice roll
    return roll

# Initialize an infinite loop to get the number of players
while True:
    # Prompt the user to enter the number of players
    players = input("Enter the number of players (2 - 4): ")
    # Check if the input is a digit
    if players.isdigit():
        # Convert the input to an integer
        players = int(players)
        # Check if the number of players is between 2 and 4
        if 2 <= players <= 4:
            # Break out of the loop if the input is valid
            break
        else:
            # Print an error message if the input is not within the range
            print("Must be between 2 - 4 players.")
    else:
        # Print an error message if the input is not a digit
        print("Invalid, try again.")

# Set the maximum score for the game
max_score = 50
# Initialize a list to store the scores of each player
player_scores = [0 for _ in range(players)]

# Print the initial scores of each player
print(player_scores)

# Initialize an infinite loop to play the game
while max(player_scores) < max_score:
    # Loop through each player
    for player_idx in range(players):
        # Print a message to indicate the start of the player's turn
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        # Print the player's current total score
        print("Your total score is:", player_scores[player_idx], "\n")
        # Initialize the player's current score for this turn
        current_score = 0
        
        # Initialize an infinite loop to roll the dice
        while True:
            # Prompt the user to decide whether to roll the dice
            should_roll = input("Would you like to roll (y)? ")
            # Check if the user wants to roll the dice
            if should_roll.lower() != "y":
                # Break out of the loop if the user doesn't want to roll
                break

            # Simulate a dice roll
            value = roll()
            # Check if the dice roll is 1
            if value == 1:
                # Print a message to indicate the end of the turn
                print("You rolled a 1! Turn done!")
                # Reset the current score to 0
                current_score = 0
                # Break out of the loop
                break
            else:
                # Add the dice roll to the current score
                current_score += value
                # Print the result of the dice roll
                print("You rolled a:", value)

            # Print the current score
            print("Your score is:", current_score)
            
        # Add the current score to the player's total score
        player_scores[player_idx] += current_score
        # Print the updated total score
        print("Your total score is:", player_scores[player_idx])

# Find the maximum score and the index of the winning player
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
# Print the result of the game
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)