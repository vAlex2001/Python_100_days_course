import Cards
import Logo
import random

def print_cards(hand):
    # Get the lines for each card and store them in a list
    card_lines = []

    # Split each card's ASCII art into lines
    for card in hand:
        card_art = hand[card]
        lines = card_art.split("\n")  # Split the card art into lines
        card_lines.append(lines)  # Add each card's lines to the list
    
    # Now print each line of the cards side by side
    for i in range(len(card_lines[0])):  # Loop over each line in the card
        line_to_print = ""
        
        # For each card, get the current line and add it to the result
        for card in card_lines:
            line_to_print += card[i].ljust(15)  # Add each line with spacing between cards
        
        print(line_to_print)  # Print all lines side by side

    print()  # Print a new line after all cards have been printed





# Print the logo
print (Logo.Logo)

# Get the cards ascii art
cards = Cards.CARDS


# Create dictionary with int as key values and the coresponding ASCII art from cards array
cards_dictionary = {}
for value in range (1, len(cards)+1):
    cards_dictionary[value] = cards[value-1]

end_game = False

while not end_game:
    # Ask the player if he wants to play another game
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_again == 'n':
        end_game = True
        break
    else:
        # Choose 2 random cards for the player
        player_card1 = random.randint(1,13)
        player_card2 = random.randint(1,13)

        # Create a dictionary for the player cards
        player_hand = {}
        player_hand = {player_card1: cards_dictionary[player_card1], player_card2: cards_dictionary[player_card2]}

        # Print player's cards
        print("Your cards:")
        print_cards(player_hand)
        
        # Choose 1 random card for the dealer
        dealer_card = random.randint(1,13)
        
        # Create a dictionary for the dealer cards
        dealer_hand = {}
        dealer_hand = {dealer_card: cards_dictionary[dealer_card]}
        
        # Print dealer's card
        print("Dealer's card:")
        print_cards(dealer_hand)
        
        # Calculate player's total score
        player_score = player_card1 + player_card2
        
        # Variable for control of drawing cards
        can_draw_card = False
        
        while not can_draw_card:            
            if player_score < 22:
                # Ask the player if he wants to draw another card
                draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if draw_card == 'y':
                    player_card3 = random.randint(1,13)
                    player_hand[player_card3] = cards_dictionary[player_card3]
                    player_score += player_card3
                    print("Your cards:")
                    print_cards(player_hand)
                elif draw_card == 'n':
                    can_draw_card = True
            else:
                can_draw_card = True
               
        # Create loop that decides randomly if the computer is drawing another card
        dealer_score = dealer_card
        
        can_draw_card = False
        
        while not can_draw_card:
            if(dealer_score < 17):
                # Generate Dealer's card
                dealer_card2 = random.randint(1,13)
                
                # Add the card to the dictionary
                dealer_hand = {dealer_card: cards_dictionary[dealer_card]}
                
                # Calculate the dealer's score
                dealer_score += dealer_card2
            else:
                can_draw_card = True
        
        # Print the final hands
        print("Your final hand:")
        print_cards(player_hand)
        print("Dealer's final hand:")
        print_cards(dealer_hand)
        
        # Print the final scores
        print(f"Your final score: {player_score}")
        print(f"Dealer's final score: {dealer_score}")
        
        # Decide the winner
        if player_score > 21:
            print("You went over. You lose!")
        elif dealer_score > 21:
            print("Dealer went over. You win!")
        elif player_score > dealer_score:
            print("You win!")
        elif player_score < dealer_score:
            print("You lose!")
        else:
            print("It's a draw!")