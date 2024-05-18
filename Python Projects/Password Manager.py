from cryptography.fernet import Fernet

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

PWD = input("What Is The Master Password? ")

key = load_key() + PWD.encode()
fer = Fernet(key)

def view():
    with open('Password.txt', 'r') as f:
        for line in f.readlines():
            Data = line.rstrip()
            user, pwd = Data.split("|")
            print("User: ", user, "| Password: ",
                   fer.decrypt(pwd.encode()).decode())



def add():
    Name = input("User Name: ")
    password = input("Password: ")

    with open('Password.txt', 'a') as f:
        f.write(Name + "|" + fer.encrypt(password.encode()).decode() + "\n")

while True:
    mode = input("Do You Want Change Password Or View The Existing One (view, add), Press Q To Quiet? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode. ")
        continue