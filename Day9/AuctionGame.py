import Logo

# Print auction game logo
print(Logo.logo)

# Dictionary to track bids
biding_dictionary = {}

end_bidding = True

while end_bidding:
    name = input("Enter your name: ")
    bid = input("Enter your bid: $")
    
    biding_dictionary[name] = bid
    
    more_bids = input("Are there any other bidders? Type 'yes' or 'no': ")
    
    if more_bids == "no":
        end_bidding = False
        print(f"The winner is {max(biding_dictionary, key=biding_dictionary.get)} with a bid of ${max(biding_dictionary.values())}.")
    else:
        # Clear the screen
        print("\033[H\033[J")