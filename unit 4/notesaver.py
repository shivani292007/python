print("Welcome to Notes Saver")

while True:
    print("\n1. Create Note")
    print("2. Read Notes")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        note = input("Write your note: ")
        with open("notes.txt", "a") as f:
            f.write(note + "\n")
        print("Note saved!")

    elif choice == "2":  # Read notes
        try:
            with open("notes.txt", "r") as f:
                print("\nYour Notes:\n")
                print(f.read())
        except FileNotFoundError:
            print("No notes found yet!")

    elif choice == "3":  # Exit
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")