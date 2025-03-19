import random
import Logo
from HangmanArt import HANGMANPICS

# Print the logo
print(Logo.banner)

# Reverse the ASCII art list 
HANGMANPICS.reverse()

# Variables to keep track of user guesses
lives = 7

# List with words to play 
world_list = ["red", "blue", "yellow"]

# Randomly select a word from the list
random_word = random.choice(world_list)

# Flag to track if the game is over or not
game_over = False

# Create a palceholder
placeholder = ""
for position in range(len(random_word)):
    placeholder+="_"

correct_letters = []

# Loop for the game
while not game_over:
    
    print(f"***** {lives} left ! *****")
    
    guess = input("Guess a letter: ")
    
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    
    # The display word based on user input
    display = ""
    
    # Check if the guess letter exists in the actual word
    for letter in random_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    
    print(display)

    if guess not in random_word:
        lives -= 1
        print(f"You've guessed {guess}, that's not in the world. You lose a life !")
        if lives == 0:
            game_over = True
            print("You lost !")
            print(f"The word was {random_word}.")
            
    if "_" not in display:
        game_over = True
        print("You win")
        
    
    print(HANGMANPICS[lives])
        