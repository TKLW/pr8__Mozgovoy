import random
import string

def generate_password(length):
<<<<<<< HEAD
    alphabet = string.ascii_letters + string.digits + string.punctuation  # Добавлены цифры и специальные символы
>>>>>>> dev
    password = .join(random.choice(alphabet) for _ in range(length))
    return password

print(generate_password(10))
