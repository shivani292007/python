print("Welcome to Number Guessing Game")

range_values = (1, 20)
print(f"Choose a secret number between {range_values[0]} and {range_values[1]}")

number = int(input("Enter the secret number: "))

print("\nNow try to guess the number!")

guesses = []
game_info = {
    "attempts": 0,
    "status": "Not Guessed"
}

guess = None

while guess != number:
    guess = int(input("Enter your guess: "))
    guesses.append(guess)
    game_info["attempts"] += 1

    if guess < number:
        print("Hint: Try a higher number!")
    elif guess > number:
        print("Hint: Try a lower number!")
    else:
        print("Correct! You guessed it.")
        game_info["status"] = "Congratulations!! You found it"

print("\n--- Game Summary ---")
print("Range was:", range_values)
print("Your guesses:", guesses)
print("Total attempts:", game_info["attempts"])
print("Game status:", game_info["status"])
print("Game Over!")