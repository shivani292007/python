import random

print(" Welcome to Dice Game – Player vs Computer ")

# Initialize scores
player_score = 0
computer_score = 0
rounds = int(input("How many rounds would you like to play? "))

for round_num in range(1, rounds + 1):
    print(f"\nRound {round_num}")

    # Roll dice for player and computer
    player_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)

    print("You rolled:", player_roll)
    print("Computer rolled:", computer_roll)

    # Decide round winner
    if player_roll > computer_roll:
        print("You win this round! ")
        player_score += 1
    elif player_roll < computer_roll:
        print("Computer wins this round! ")
        computer_score += 1
    else:
        print("It's a tie this round! ")

    # Show current score
    print(f"Score → You: {player_score} | Computer: {computer_score}")

# Final result
print("\n  Final Result ")
if player_score > computer_score:
    print("Congratulations! You are the overall winner!")
elif player_score < computer_score:
    print("Computer wins the game! Better luck next time!")
else:
    print("It's a tie overall!")

print("\nThanks for playing the Dice Game!")