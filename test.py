import random

def number_guessing_game():
    target_number = random.randint(1, 100)
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("You have 10 attempts to guess the number between 1 and 100.")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))

            if guess == target_number:
                print(f"Congratulations! You guessed the number {target_number} correctly in {attempt} attempts!")
                break
            elif guess < target_number:
                print("Your guess is too low.")
            else:
                print("Your guess is too high.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

    else:
        print(f"Sorry, you've used all your attempts. The correct number was {target_number}.")
number_guessing_game()


