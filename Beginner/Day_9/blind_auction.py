from replit import clear
from blind_auction_art import logo


def collect_bids():
    bids = {}
    next_person = True
    while next_person:
        name = input("What is your name?: ")
        bid = round(float(input("What is your bid?: $")), 2)
        bids[name] = bid
        if input("Are there any other bidders? Type 'yes' or 'no'.\n").strip() == 'yes':
            clear()
        else:
            next_person = False
    return bids


def find_highest_bidder(bids):
    highest_bid = 0
    highest_bidder = ''

    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            highest_bidder = bidder

    highest_bid = '{:0.2f}'.format(highest_bid)
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")


print(logo)
print("Welcome to the secret auction program.")

complete_bids = collect_bids()
find_highest_bidder(complete_bids)
