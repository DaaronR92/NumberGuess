import random  # Import the random module to generate random numbers

# Function for the guessing game
def guess_number():
    # Pick a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0  # Keep track of how many guesses the player has made
    guessed = False  # This flag will become True when the player guesses correctly

    print("Welcome to the Number Guessing Game!")  # Friendly greeting
    print("I have selected a number between 1 and 100.")  # Inform the player about the game

    # The game will keep running until the player guesses correctly
    while not guessed:
        try:
            # Ask the player to make a guess (input is expected to be a number)
            guess = int(input("Enter your guess: "))
            attempts += 1  # Count how many guesses the player has made so far

            # Give hints based on the player's guess
            if guess < number_to_guess:
                print("Too low! Try again.")  # Let the player know if their guess is too low
            elif guess > number_to_guess:
                print("Too high! Try again.")  # Let the player know if their guess is too high
            else:
                # If the guess is correct, congratulate the player and show how many attempts it took
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                guessed = True  # Set the flag to True to end the game loop
        except ValueError:
            # In case the player enters something that's not a number, handle the error
            print("Please enter a valid number.")  # Friendly reminder to input a valid number

# Run the guessing game when the script is executed
if __name__ == "__main__":
    guess_number()  # Start the game
