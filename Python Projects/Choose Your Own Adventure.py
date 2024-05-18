Name = input("Type Your Name ")
print('Welcome', Name,"To This Adventure")

Answer = input(
    "You Are On A Dirt Road, It Has Come To An End And You Can Go Left Or Right. Which Way Would You Like To Go ? ").lower()
if Answer == "left":
    Answer= input("You Come To A River, You Can Walk Around And Swim Across ? Type Walk To Walk Around And Swim To Swim Across ").lower()
    if Answer=="swim":
        print("You Were Eaten By An Alligator ")       
    elif Answer=="walk":
        print("You Walk Around Of River But Got Robbed By Robber. Well, It Not Bad As Eaten Alive By An Alligator ")
    else:
        print("Choose A Valid Option. You Lose ")
elif Answer == "right":
    Answer = input("You Find A Big Gate. Do You Want to Go Inside Or Walk Around It ? Type Inside To Enter The Gate Or Type Walk To Walk Around It ").lower()
    if Answer == "inside":
        print("You Tried To Enter The Gate But Guard Thought You Were Suspicious And Killed You. That Place Was Under Terrorist Organization. You Lose ")
    elif Answer == "walk":
        print("You walk Around from The Gate Successfully But Two Bengal Tigers Attacked You And Killed You. You Lose ")
    else:
        print("Choose A Valid Option. You Lose")
else:
    print("Choose A Valid Option. You Lose")

print("Thank You For Trying ", Name)