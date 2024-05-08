import random

def get_user_input(prompt):
    """Get user input and handle special commands like 'x', 'n', and 's'."""
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'x':
            print("Exiting the game.")
            exit()
        elif user_input.lower() == 'n':
            return 'n'
        elif user_input.lower() == 's':
            return 's'
        try:
            return int(user_input)
        except ValueError:
            print("Please enter a valid number, 'x' to exit, 'n' to start a new game, or 's' to show the secret number.")

def play_game():
    """Play a single game round."""
    number_to_guess = random.randint(1, 20)  # Pick a random number between 1 and 20.
    guesses = 0
    print("\nGuess the secret number between 1 and 20.")

    while True:
        user_guess = get_user_input("Enter your guess: ")
        if user_guess == 's':
            print(f"Cheating! The secret number is {number_to_guess}.")
            continue
        elif user_guess == 'n':
            return False  # Return False to indicate the user wants to start a new game.
        guesses += 1
        if user_guess > number_to_guess:
            print(f"Your guess is too high. Guess again. (You've guessed {guesses} times.)")
        elif user_guess < number_to_guess:
            print(f"Your guess is too low. Guess again. (You've guessed {guesses} times.)")
        else:
            print(f"Good job! You guessed the number in {guesses} guesses.")
            return True  # Return True to indicate the user has guessed correctly.

def main():
    """Main function to manage game sessions."""
    keep_playing = True
    while keep_playing:
        game_result = play_game()
        if game_result:
            keep_playing = input("Do you want to play another game? (yes/no): ").lower() == 'yes'
        else:
            keep_playing = input("Start a new game? (yes/no): ").lower() == 'yes'

if __name__ == "__main__":
    main()
