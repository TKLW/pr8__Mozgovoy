import random
import string

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation  # Добавлены цифры и специальные символы
    password = ''.join(random.choice(alphabet) for _ in range(length))  # Исправлено на ''
    return password

print(generate_password(10))
