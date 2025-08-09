import random
import string

def generate_password(length):
    if length < 4:
        return "Password length must be at least 4."

    # Characters to choose from
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    # Ensure at least one from each category
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest randomly
    all_chars = upper + lower + digits + special
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    return ''.join(password)

# Main program
length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))
