import random

print("Welcoome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number_to_guess = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5
    
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    
    if guess == number_to_guess:
        print(f"You got it! The answer was {number_to_guess}.")
        break
    elif guess < number_to_guess:
        print("Too low.")
    else:
        print("Too high.")
    
    attempts -= 1
    if attempts == 0:
        print("You've run out of guesses, you lose.")
    else:
        print("Guess again.")