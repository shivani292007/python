score = 0
print("Welcome to Python MCQ Quiz")

print("\n1. What is the extension of Python file?")
print("a) .py")
print("b) .java")
print("c) .html")
print("d) .cpp")
ans = input("Enter your answer: ")
if ans.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n2. Which keyword is used for function in Python?")
print("a) fun")
print("b) define")
print("c) def")
print("d) function")
ans = input("Enter your answer: ")
if ans.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n3. Which data type is used for numbers?")
print("a) int")
print("b) str")
print("c) list")
print("d) tuple")
ans = input("Enter your answer: ")
if ans.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

balance = 2000
while True:
    print("\n===== ATM Menu =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":
        amt = input("Enter amount to deposit: ")
        if amt.isdigit():
            amt = int(amt)
            balance += amt
            print("Deposited:", amt)
            print("New balance:", balance)
        else:
            print("Please enter numbers only.")

    elif choice == "3":
        amt = input("Enter amount to withdraw: ")
        if amt.isdigit():
            amt = int(amt)
            if amt <= balance:
                balance -= amt
                print("Withdrawn:", amt)
                print("New balance:", balance)
            else:
                print("Not enough balance!")
        else:
            print("Please enter numbers only.")

    elif choice == "4":
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice, try again.")