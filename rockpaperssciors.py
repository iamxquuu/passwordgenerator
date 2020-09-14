from random import randint
rock_paper_scissors = ["Rock", "Paper", "Scissors"]
computer_choose = rock_paper_scissors[randint(0, 2)]

player = False
while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer_choose:
        print("Tie")
    elif player == "Rock":
        if computer_choose == "Paper":
            print("You lose!", computer_choose, "covers", player)
        else:
            print("You win!", player, "smashes", computer_choose)
    elif player == "Paper":
        if computer_choose == "Scissors":
            print("You lose!", computer_choose, "cut", player)
        else:
            print("You win!", player, "covers", computer_choose)
    elif player == "Scissors":
        if computer_choose == "Scissors":
            print("You lose!", computer_choose, "smashes", player)
        else:
            print("You win!", player, "cut", computer_choose)
    else:
        print("Something went wrong")
    player = False
    computer_choose = rock_paper_scissors[randint(0, 2)]



