print("Welcome To My Quiz")
playing = input("Do Want To Play? ")
print(playing)

if playing.lower() != "yes":
    quit()
    
print("Okay, Let's Play :) ")
score = 0

print("Question No 1!")

answer = input("What Is The Capital Of Pakistan? ")
if answer.lower() == "islamabad":
    print("Correct!")
    score += 1
else:
    print("Your Answer Is Incorrect")

print("Question No 2!")
answer = input("What Is The Capital Of Sindh? ")
if answer.lower() == "karachi":
    print("Correct!")
    score += 1
else:
    print("Your Answer Is Incorrect")

print("Question No 3!")
answer = input("What Is The Capital Of Punjab? ")
if answer.lower() == "lahore":
    print("Correct!")
    score += 1
else:
    print("Your Answer Is Incorrect")

print("Question No 4!")
answer = input("What Is The Capital Of Balochistan? ")
if answer.lower() == "quetta":
    print("Correct!")
    score += 1
else:
    print("Your Answer Is Incorrect")

print("Question No 5!")
answer = input("What Is The Capital Of K.P.K? ")
if answer.lower() == "peshawar":
    print("Correct!")
    score += 1
else:
    print("Your Answer Is Incorrect")

print("You Got " + str(score) + " Question Correct!")