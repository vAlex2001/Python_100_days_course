import Logo_Art
import game_data
import random

# This is the start of the game
# Print the logo ASCII art.

print(Logo_Art.logo)

# Create a variable to store the score
score = 0

# Create a variable to store the game status
game_over = False

# Create a variable to store the first account
account_a = random.choice(game_data.data)

# Create a variable to store the second account
account_b = random.choice(game_data.data)

# Check if the two accounts are the same
while account_a == account_b:
    account_b = random.choice(game_data.data)
    
# Remove the choices from the list
game_data.data.remove(account_a)
game_data.data.remove(account_b)

# Create a while loop to keep the game running until the user gets it wrong or the list ends
while not game_over and len(game_data.data) > 0:
    # Print the account A information
    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.")

    # Print the VS logo
    print(Logo_Art.versus_symbol)

    # Print the account B information
    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.")

    # Ask the user to guess who has more followers
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get the follower count of each account
    follower_count_a = account_a['follower_count']
    follower_count_b = account_b['follower_count']

    # Check if the user guess is correct
    if user_guess == 'a' and follower_count_a > follower_count_b:
        # Update the score
        score += 1
        
        # Print the score
        print(f"You're right! Current score: {score}")
        
        # Keep the correct guess account and remove the other account from the list
        game_data.data = [item for item in game_data.data if item["name"] != account_b["name"]]
        account_b = random.choice(game_data.data)
        
        # Check if the two accounts are the same
        while account_a == account_b:
                account_b = random.choice(game_data.data)

    elif user_guess == 'b' and follower_count_b > follower_count_a:
        # Update the score
        score += 1
        
        # Print the score
        print(f"You're right! Current score: {score}")
        
        # Keep the correct guess account and remove the other account from the list
        game_data.data = [item for item in game_data.data if item["name"] != account_a["name"]]
        account_a = random.choice(game_data.data)
        
        # Check if the two accounts are the same
        while account_a == account_b:
                account_a = random.choice(game_data.data)

    else:
        # Print the final score
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True