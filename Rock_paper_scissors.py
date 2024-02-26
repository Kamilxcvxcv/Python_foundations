import random

while True:

    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)  # computer picks random choice from choices
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()  # string are case-sensitive so if you would write it with capitalize letter it would be wrong  by adding .lower it takes player input and makes it lower so that it matches

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You won!")
    elif player == "scissors":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You won!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You won!")
    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("Bye!")
