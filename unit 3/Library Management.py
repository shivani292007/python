def play_game():
    choices = ["rock", "paper", "scissors"]
    print("Welcome to Rock-Paper-Scissors!")

    while True:
        user = input("\nEnter your choice (rock/paper/scissors or quit): ").lower()
        
        if user == "quit":
            print("Thanks for playing")
            break
        
        if user not in choices:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        computer = random.choice(choices)
        print(f"You chose: {user}")
        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a Tie!")
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("You Win!")
        else:
            print("You Lose!")

play_game()