import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choices = [rock, paper, scissors]
userChoice = int(input("What do you choose? 1 for Rock, 2 for Paper, 3 for Scissors: ")) - 1
comChoice = random.randint(0,2)
if userChoice > 2 or userChoice < 0:
    print("Invalid selection!")
elif (userChoice == 0 and comChoice == 2) or (userChoice == 1 and comChoice == 0) or (userChoice == 2 and comChoice == 1):
    print(f"User Win\nUser:\n{choices[userChoice]}\nCom:\n{choices[comChoice]}")
elif userChoice == comChoice:
    print(f"Tie Game\nUser:\n{choices[userChoice]}\nCom:\n{choices[comChoice]}")
else:
    print(f"Com Wins\nUser:\n{choices[userChoice]}\nCom:\n{choices[comChoice]}")