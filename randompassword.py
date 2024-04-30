import secrets
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    # Define character sets based on user criteria
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    digit_chars = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''

    # Combine character sets
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    # Ensure the password length is at least 4 characters
    length = max(length, 4)

    # Generate password using secrets module for better security
    password = ''.join(secrets.choice(all_chars) for _ in range(length))

    return password

# Example usage
password = generate_password(length=16, use_uppercase=True, use_numbers=True, use_special_chars=True)
print("Generated Password:", password)
