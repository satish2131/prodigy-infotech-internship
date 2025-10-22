
import random

def guessing_game():
    print(" === Guess the Number Game ===")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is? 🤔")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Ask user for a guess
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"🎉 Congratulations! You guessed it right in {attempts} attempts.")
                print(f"The secret number was {secret_number}.")
                break

        except ValueError:
            print("⚠️ Please enter a valid number!")

if __name__ == "__main__":
    guessing_game()
