#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

### Imports ###
import art
import random
from os import system

### Global Variables ###
EASY_TURNS = 10
HARD_TURNS = 5
playAgain = True

### Function Library ###
# Def difficulty - set the number of turns the user gets.
def difficultySetter():
  diff = input("Choose a difficulty: 'Easy' or 'Hard' ").lower()
  if diff == 'easy':
    return EASY_TURNS
  elif diff == 'hard':
    return HARD_TURNS

# Define computers chosen number
pickedNumber = 0
def pickNumber():
  pick = random.randint(1, 100)
  return pick

# Define guess to get a players guess
def guess(t):
  guess = int(input("Pick a number: "))

  if guess == pickedNumber:
    print("You win!")
    return True
  elif guess > pickedNumber:
    print("Too high.")
    return checkLives(t)
  elif guess < pickedNumber:
    print("Too low.")
    return checkLives(t)

# Define life checker
def checkLives(t):
  if t - 1 == 0:
    print("You've run out of tries.")
    return True
  else:
    print(f"You have {t-1} turns left.")
    return False

# Define play again
def again():
  again = input("Would you like to play again? 'Y' or 'N': ").lower()
  if again == 'y':
    system('cls')
    return True
  else:
    print("Thanks for playing!")
    return False

### Main Function ###
while playAgain == True:
  gameOver = False
  print(art.logo)
  
  print("Welcome to the Number Guesser!")
  turns = difficultySetter()
  print("I'm thinking of a number from 1 to 100.")
  pickedNumber = pickNumber()
  
  while gameOver == False:
    gameOver = guess(turns)
    if gameOver == False:
      turns -= 1

  playAgain = again()