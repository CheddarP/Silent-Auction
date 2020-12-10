from art import logo

print(logo)
print("Welcome to the Silent Auction!")

bids = {}

def find_highest(bidding_records):
    highest = 0
    winner = ""
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if highest < bid_amount:
            highest = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bet of ${highest}!!!")


should_continue = True
while should_continue:
    name = input("What's your name?: ")
    price = int(input("How much do you want to bid?: $"))
    bids[name] = price

    keep_going = input("Are there any other users who want to bid? (yes or no) :").lower()
    if keep_going == 'no':
        should_continue = False
        find_highest(bids)


