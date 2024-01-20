import random
import string

def generate_password():
    uppercase_chars = string.ascii_uppercase
    lowercase_chars = string.ascii_lowercase
    numeric_chars = string.digits
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    all_chars = uppercase_chars + lowercase_chars + numeric_chars + special_chars

    password = ''.join(random.choice(all_chars) for _ in range(8))

    return password

# Test
generated_password = generate_password()
print('Generated Password:', generated_password)
