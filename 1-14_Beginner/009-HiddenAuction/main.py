import os
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)

auctionBids = {}
moreBidders = True
high_Name = ""
high_Bid = 0

while moreBidders == True:
  bidderName = input("What is your name? ")
  amount = int(input("How much do you bid? $"))

  auctionBids[bidderName] = amount

  os.system("cls")
  
  newBidder = input("Are there any more bidders? Yes or No ").lower()
  if newBidder == "no":
    moreBidders = False

for bid in auctionBids:
  if auctionBids[bid] > high_Bid:
    high_Name = bid
    high_Bid = auctionBids[bid]

print(f"The winner is {high_Name} with a bid of ${high_Bid}!")