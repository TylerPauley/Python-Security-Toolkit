import re

password = input("Enter a password you'd like to see if it's strong >> ")

password_length = len(password)
score = 0

if re.search(r'[a-z]', password):  # Lowercase letters
    score += 1
if re.search(r'[A-Z]', password):  # Uppercase letters
    score += 1
if re.search(r'[0-9]', password):  # Numbers
    score += 1
if re.search(r'[@$!%*?&]', password):  # Special characters
    score += 1

if score == 1:
    print("Weak password. Only lowercase letters.")
elif score == 2:
    print("Moderate password. Contains at least one uppercase and lowercase letters.")
elif score == 3:
    print("Good password. Contains letters and numbers.")
elif score == 4:
    if password_length >= 8:
        print("Strong password. Contains uppercase, lowercase, numbers, and special characters.")
    else:
        print("Almost strong! Make the password longer than 8 characters.")
else:
    print("Very weak password. Consider using a mix of different characters.")
