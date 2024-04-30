import random

number_to_guess = random.randint(1, 20)  # Pick a random number between 1 and 20.
guesses = 0

print("Guess the secret number between 1 and 20.")

while True:
    try:
        user_guess = int(input("Enter your guess: "))  # Prompt for a guess.
        guesses += 1  # Increment the guess counter.
        if user_guess > number_to_guess:
            print(f"Your guess is too high. Guess again. (You've guessed {guesses} times.)")
        elif user_guess < number_to_guess:
            print(f"Your guess is too low. Guess again. (You've guessed {guesses} times.)")
        else:
            print(f"Good job! You guessed the number in {guesses} guesses.")
            break  # If correct, congratulate the user and end the loop.
