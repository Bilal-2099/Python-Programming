# First I Introduce YOu To The Game
print("Welcome To My Quiz")
# Ask If You Wanna Play
playing = input("Do Want To Play? ")
print(playing)
# If Yes Than Continue Or Quit
if playing.lower() != "yes":
    quit()
    
print("Okay, Let's Play :) ")
# Here I Made Variable Called Score For Count The Score
score = 0

print("Question No 1!")
# I Ask The Question And Than With If Else I Add 1 To Score For Right Answer
answer = input("What Is The Capital Of Pakistan? ")
if answer.lower() == "islamabad":
    print("Correct!")
    score += 1
else:
    print("Your Answer Is Incorrect")

# Same Goes For Other Question
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
    
# In the End I Tell Them Their Score
print("You Got " + str(score) + " Question Correct!")