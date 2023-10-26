############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
import art
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

anotherHand = True

def dealcard():
  return cards[random.randint(0, len(cards)-1)]

def handTotal(hand):
  return sum(hand)

while anotherHand == True:
  # clear Screen and print logo
  print(art.logo)
  playerHand = []
  dealerHand = []

  # Deal card to player, dealer, player, dealer
  playerHand.append(dealcard())
  playerHand.append(dealcard())
  dealerHand.append(dealcard())
  dealerHand.append(dealcard())

  stay = False
  playerLost = False
  dealerLost = False

  # Players Turn
  while stay == False:
    playerHandScore = handTotal(playerHand)
    dealerHandScore = handTotal(dealerHand)
    print(f"\nPlayer: {playerHand} = {playerHandScore}")
    print(f"Dealer: [{dealerHand[0]}, _]")
    
    if playerHandScore == 21:
      print("You're at 21. You stay.")
      stay = True
    elif playerHandScore > 21:
      # Check for an 11, convert to 1 if playerHand has an 11
      if 11 in playerHand:
        playerHand.remove(11)
        playerHand.append(1)
        stay = False
      else:
        print("Sorry, you busted. You lose.")
        playerLost = True
        stay = True
    else:
      action = input("Would you like to hit or stay? ").lower()
      if action == "hit":
        playerHand.append(dealcard())
      elif action == "stay":
        stay = True


  # Create dealer logic (if < 16 Hit, else Stand)
  dealerStay = False
  while dealerStay == False:
    dealerHandScore = handTotal(dealerHand)
    print(f"\nPlayer: {playerHand} = {playerHandScore}")
    print(f"Dealer: {dealerHand} = {dealerHandScore}")
    
    if playerHandScore > 21:
      print("Dealer Stays.")
      dealerStay = True
    elif dealerHandScore < 16:
      print("Dealer Hits.")
      dealerHand.append(dealcard())
    elif dealerHandScore >= 16 and dealerHandScore <= 21:
      print("Dealer Stays.")
      dealerStay = True
    elif dealerHandScore > 21:
      if 11 in dealerHand:
        dealerHand.remove(11)
        dealerHand.append(1)
        dealerStay = False
      else:
        print("Dealer Busts.")
        dealerLost = True
        dealerStay = True
  
  # Check to see who won.
  print("\n")
  if playerLost == True:
    print("You lose. Better luck next time.")
  elif dealerLost == True:
    print("You win! Congratulations!")
  elif playerHandScore < dealerHandScore:
    print("You lose. Better luck next time.")
  elif playerHandScore > dealerHandScore:
    print("You win! Congratulations!")
  elif playerHandScore == dealerHandScore:
    print("Push.")
  
  # Deal another hand?
  again = input("\nWould you like to play another hand? Y or N  ").lower()
  if again == 'y':
    os.system('cls')
    anotherHand = True
  else:
    anotherHand = False
    print("Thanks for playing!")