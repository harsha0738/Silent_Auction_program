from art import logo
print(logo)
def find_highest_bidder(bids):
  highest_bid = 0
  winner = ""
  for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder

  print(f"the winner is {winner} with a bid amount of {highest_bid}")



continue_game = True

bids = {}

while continue_game:
  name = input("enter your name :")
  price = int(input("enter the bid amount :"))
  bids[name] = price
  should_continue = input("are there any bidders left? type 'yes' or 'no': \n")
  if should_continue == "yes":
    print("\n" * 20)
  elif should_continue == "no":
    continue_game = False
    find_highest_bidder(bids)
  else:
    print("error occured")






