import random

optList = {"R": "Rock", "P": "Paper", "S": "Scissors"}
while True:
    prompt = input("Enter either R, P or S for Rock, Paper or Sciscors ")
    if(prompt=="R"):
        prompt = "Rock"
    elif(prompt=="P"):
        prompt = "Paper"
    elif(prompt=="S"):
        prompt = "Scissors"
    else:
        print("Invalid choice")
        break

    com = random.choice(list(optList))
    print(f"Player ({prompt}) : CPU ({optList[com]})")
    if(prompt==optList[com]):
        print("It's a tie, start again!")
    elif(prompt=="Rock" and com=="S"):
        print("Player Wins")
        break
    elif(prompt=="Paper" and com=="R"):
        print("Player Wins")
        break
    elif(prompt=="Scissors" and com=="P"):
        print("Player Wins")
        break
    else:
        print("CPU Wins")
        break



    
    
   