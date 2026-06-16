# Number Guessing Game

A simple command-line Number Guessing Game built with Python. The computer randomly selects a number between **1 and 100**, and the player must guess the correct number within a limited number of attempts based on the selected difficulty level.

## Features

* Random number generation between **1 and 100**
* Three difficulty levels:

  * **Easy** – 10 chances
  * **Medium** – 5 chances
  * **Hard** – 3 chances
* Input validation for non-numeric values
* Hints after each incorrect guess
* Tracks the number of attempts used
* Ends when the player wins or runs out of chances

## Requirements

* Python 3.x

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the following command:

```bash
python app.py
```

## How to Play

1. Start the game.
2. Choose a difficulty level:

   * `1` for Easy
   * `2` for Medium
   * `3` for Hard
3. Enter a number between **1 and 100**.
4. The game will tell you whether the secret number is greater or less than your guess.
5. Continue guessing until:

   * You guess the correct number, or
   * You run out of attempts.

## Example

```text
Welcome To The Number Guessing Game!
I'm thinking of a number between 1 and 100.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter the difficulty level: 2

Great! You have selected the Medium difficulty level.
Let's start the game!

Guess The Number: 50
Incorrect! The number is greater than 50
Attempts remaining: 4

Guess The Number: 75
Congratulations! You guessed the correct number in 2 attempts.
```

## Project Structure

```text
├── app.py
└── README.md
```

## Learning Concepts

This project demonstrates:

* Variables
* User Input
* Conditional Statements (`if`, `elif`, `else`)
* Loops (`while`)
* Dictionaries
* Random Number Generation
* Input Validation
* Basic Game Logic

**GitHub Repository:**  
[Number Guessing Game Script](https://github.com/Bilal-2099/Python-Programming/tree/main/Python%20Projects/Number%20Guesser)
