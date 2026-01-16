import random

loop = True
while loop:
    bot_choice = random.choice(["R", "P", "S"])
    player_choice = input("Choose R,P,S: ")
    print(f"The bot chosed: {bot_choice}")
    if player_choice == "Exit":
        print("Leaving the game...")
        loop = False
        break
    else:
        if player_choice == bot_choice:
            print("It's a DRAW!")
        elif player_choice == "S" and bot_choice == "P" or player_choice == "P" and bot_choice == "R" or player_choice == "R" and bot_choice == "S":
            print("You WON!")
        else:
            print("You lost!")
            print("You sucks")