print("Password Strength Checker")

password = input("Enter your password: ")
length = len(password)

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_chars = "!@#$%^&*()-_=+?/"

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special_chars:
        has_special = True

if length < 6:
    print("Password is Weak (Too short)")
elif has_upper and has_lower and has_digit and has_special and length >= 10:
    print("Password is Very Strong")
elif has_upper and has_lower and has_digit and has_special:
    print("Password is Strong")
elif has_upper and has_lower and has_digit:
    print("Password is Medium")
else:
    print("Password is Weak")