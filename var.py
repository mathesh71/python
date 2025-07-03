# Variable to store the secret number
secret_number = 7
attempts = 3  # Maximum number of tries

print("Welcome to the Number Guessing Game!")
print("You have 3 attempts to guess the correct number between 1 and 10.")

# Loop to give the player multiple attempts
for attempt in range(1, attempts + 1):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    # Conditional statements to check the guess
    if guess == secret_number:
        print("🎉 Congratulations! You guessed the right number!")
        break
    elif guess < secret_number:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")

# If the loop ends without a correct guess
else:
    print(f"❌ Sorry, you're out of attempts. The secret number was {secret_number}.")
