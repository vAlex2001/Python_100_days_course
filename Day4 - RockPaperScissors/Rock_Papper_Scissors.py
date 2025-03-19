import random

# Rock
Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

options = [Rock, Paper, Scissors]

human_choice = int(input("Choose your option 0 - > Rock, 1 -> Paper, 2 -> Scissors : "))

if human_choice > 2 or human_choice < 0:
    print("Wrong value.")
else:
    computer_choice = random.randint(0,2)
    print("Human Choice: \n" + options[human_choice] + "\n")
    print("Computer Choice: \n" + options[computer_choice] + "\n")
    if human_choice == computer_choice:
        print("Draw")
    elif human_choice == 0 and computer_choice == 2:
        print("Win")
    elif human_choice == 2 and computer_choice == 0:
        print("Loose")
    elif human_choice > computer_choice:
        print("Win")
    elif human_choice < computer_choice:
        print("Loose")
