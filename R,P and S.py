import random

#Rock paper scissors game

print("Rock, paper and scissors game")

print("Hello welcome to the game, you will be playing against a bot")

options = ["R", "P" , "S"]

x = 0
while x <= 10:

    player1 = input("R, P or S(please enter one of the letters shown prior): ").upper()

    player2 = random.choice(options)

    if player1 not in options:
        print("Invalid entry")

    elif player1 == player2:
        print(f"you selected {player1}")
        print(f"Bot selected {player2}")
        print("It was a draw, better luck next time.")

    elif player1 == "R" and player2 == "P" or player1 == "P" and player2 == "S" or player1 == "S" and player2 == "R":
        print(f"you selected {player1}")
        print(f"Bot selected {player2}")
        print("Bot wins")

    elif player1 == "P" and player2 == "R" or player1 == "S" and player2 == "P" or player1 == "R" and player2 == "S":
        print(f"you selected {player1}")
        print(f"Bot selected {player2}")
        print("You win")

    else:
        ("error occured")

  








