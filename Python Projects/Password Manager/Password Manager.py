# Import the Fernet class from the cryptography.fernet module, which is used for symmetric encryption
from cryptography.fernet import Fernet

# This function generates a key and writes it to a file named "key.key"
# It's currently commented out, so it won't be executed
'''def write_key():
    # Generate a key using Fernet's generate_key method
    key = Fernet.generate_key()
    # Open a file named "key.key" in binary write mode
    with open("key.key", "wb") as key_file:
        # Write the generated key to the file
        key_file.write(key)'''

# This function loads the key from the "key.key" file
def load_key():
    # Open the "key.key" file in binary read mode
    file = open("key.key", "rb")
    # Read the key from the file
    key = file.read()
    # Close the file
    file.close()
    # Return the key
    return key

# Load the key using the load_key function
key = load_key()
# Create a Fernet object using the loaded key
fer = Fernet(key)

# This function views the existing passwords
def view():
    # Open the "passwords.txt" file in read mode
    with open('passwords.txt', 'r') as f:
        # Iterate over each line in the file
        for line in f.readlines():
            # Remove the newline character from the end of the line
            Data = line.rstrip()
            # Split the line into user and password using the "|" character as a separator
            user, passw = Data.split("|")
            # Decrypt the password using the Fernet object and print it
            print("User:", user, ", Password:", fer.decrypt(passw.encode()).decode())

# This function adds a new password
def add():
    # Get the account name and password from the user
    name = input('Account Name: ')
    pwd = input('Password: ')

    # Open the "passwords.txt" file in append mode
    with open('passwords.txt', 'a') as f:
        # Encrypt the password using the Fernet object and write it to the file
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# Main loop
while True:
    # Ask the user what they want to do
    mode = input("Would You Like To Add A New Password Or View Existing Ones(view, add), Press q To Quit?").lower()
    # If the user wants to quit, break out of the loop
    if mode == "q":
        break

    # If the user wants to view passwords, call the view function
    if mode == "view":
        view()
    # If the user wants to add a password, call the add function
    elif mode == "add":
        add()
    # If the user enters anything else, print an error message and continue to the next iteration
    else:
        print('Invalid Mode.')
        continue