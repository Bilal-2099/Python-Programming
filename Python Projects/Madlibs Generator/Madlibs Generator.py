# Open the file "story.txt" in read mode
with open("story.txt", "r") as f:
    # Read the entire file into the variable story
    story = f.read()

# Initialize an empty set to store unique words
words = set()
# Initialize a variable to keep track of the start of a word
start_of_word = -1

# Define the target characters to identify words
target_start = "<"
target_end = ">"

# Iterate over each character in the story
for i, char in enumerate(story):
    # If the character is the start of a word, update the start_of_word variable
    if char == target_start:
        start_of_word = i

    # If the character is the end of a word and start_of_word is not -1, extract the word
    if char == target_end and start_of_word != -1:
        # Extract the word from the story using slicing
        word = story[start_of_word: i + 1]
        # Add the word to the set of unique words
        words.add(word)
        # Reset the start_of_word variable
        start_of_word = -1

# Initialize an empty dictionary to store answers
answers = {}

# Iterate over each unique word
for word in words:
    # Prompt the user to enter a word for the current word
    answer = input("Enter a word for " + word + ": ")
    # Store the user's answer in the answers dictionary
    answers[word] = answer

# Iterate over each unique word again
for word in words:
    # Replace the word in the story with the user's answer
    story = story.replace(word, answers[word])

# Print the modified story
print(story)