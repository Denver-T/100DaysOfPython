import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

moveset = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!")

player_choice = int(
    input(
        "What do you choose? \n1 for Rock\n2 for Paper\n3 for Scissors\nYour choice: "
    )
)

comp_move = random.choice(moveset)

# player chose Rock
if player_choice == 1:
    print("You chose Rock")
    print(rock)
    print("Computer chose... ")
    print(comp_move)
    if comp_move == scissors:
        print("Scissors!")
        print("You won! Congrats!")
    elif comp_move == rock:
        print("Rock!")
        print("DRAW!")
    else:
        print("Paper")
        print("You lose.")

# Player chose Paper
if player_choice == 2:
    print("You chose Paper")
    print(paper)
    print("Computer chose... ")
    print(comp_move)
    if comp_move == rock:
        print("Rock!")
        print("You won! Congrats")
    elif comp_move == paper:
        print("Paper")
        print("DRAW!")
    else:
        print("Scissors!")
        print("You lose.")

# Player chose Scissors
if player_choice == 3:
    print("You chose Scissors")
    print(scissors)
    print("Computer chose... ")
    print(comp_move)
    if comp_move == paper:
        print("Paper")
        print("You won! Congrats!")
    elif comp_move == scissors:
        print("Scissors!")
        print("DRAW!")
    else:
        print("Rock!")
        print("You lose.")
