password = input("Enter a password: ")
checks = [
    len(password) >= 8,
    any(char.islower() for char in password),
    any(char.isupper() for char in password),
    any(char.isdigit() for char in password),
    any(not char.isalnum() for char in password),
]
score = sum(checks)
if score <= 2:
    print("Weak password")
elif score <= 4:
    print("Moderate password")
else:
    print("Strong password")