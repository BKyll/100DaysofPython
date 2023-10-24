# IMPORTS
import art
import game_data
import random
#from replit import clear
import os

# GLOBAL VARIABLES
PLAY_AGAIN = True
GAME_OVER = False


# FUNCTIONS
def get_insta_account():
  """Returns a random instagram accounts information."""
  return game_data.data[random.randint(0, len(game_data.data) - 1)]

def print_choice(choice):
  """Returns a formatted version of 'choice' instagram information."""
  return f"{choice['name']} is a {choice['description'].lower()} from {choice['country']}."

# MAIN
while PLAY_AGAIN == True:
  score = 0
  choice1 = get_insta_account()

  #clear()
  os.system('cls')
  print(art.logo)

  # Game Loop
  while GAME_OVER == False:
    print(f"Compare A: {print_choice(choice1)}")
    
    print(art.vs)
    
    choice2 = get_insta_account()
    while choice1 == choice2:
      choice2 = get_insta_account()
    print(f"Against B: {print_choice(choice2)}")

    player_choice = input("\n\nWhich account has more followers? A or B? ").lower()

    winner = ''
    winner_dict = ''

    if choice1['follower_count'] > choice2['follower_count']:
      winner = 'a'
    else:
      winner = 'b'
      choice1 = choice2

    if player_choice == winner:
      score += 1
      # clear()
      os.system('cls')
      print(art.logo)
      print(f"Correct! Current score: {score}")

    else:
      print(f"That is incorrect. You scored {score}.")
      GAME_OVER = True

  play_again = input("Would you like to play again? ").lower()
  if play_again == 'no':
    PLAY_AGAIN = False
  else:
    GAME_OVER = False
