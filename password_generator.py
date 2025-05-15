import random
import string

def generate_password(length):
    alphabet = string.ascii_lowercase
    password = .join(random.choice(alphabet) for _ in range(length))
    return password

print(generate_password(10))
