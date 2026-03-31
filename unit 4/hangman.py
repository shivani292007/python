import random

print("Welcome to Hangman Game!")

words = ["python", "hangman", "programming", "developer", "computer"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

while attempts > 0 and "_" in guessed:
    print("\nWord: ", " ".join(guessed))
    print("Attempts left:", attempts)
    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

if "_" not in guessed:
    print("\nYou Win! The word was:", word)
else:
    print("\nYou Lose! The word was:", word)