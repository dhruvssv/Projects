import random
choices=["rock","paper" , "scissors"]
cpu=random.choice(choices)
player=None
while player not in choices:
    player=input('Enter rock,paper,scissors').lower()
if player==choices:
    print("player: ",player)
    print("cpu: ",cpu)
    print("Tie!")
elif player=="rock":
    if cpu=="paper":
        print("player: ",player)
        print("cpu: ",cpu)
        print("You lose!")
    elif cpu=="scissors":
        print("player: ",player)
        print("cpu: ",cpu)
        print("You win!")
elif player=="paper":
    if cpu=="rock":
        print("player: ",player)
        print("cpu: ",cpu)
        print("You win!")
    elif cpu=="scissors":
        print("player: ",player)
        print("cpu: ",cpu)
        print("You win!")
elif player=="scissors":
    if cpu=="paper":
        print("player: ",player)
        print("cpu: ",cpu)
        print("You win!")
    elif cpu=="rock":
        print("player: ",player)
        print("cpu: ",cpu)
        print("You win!")

