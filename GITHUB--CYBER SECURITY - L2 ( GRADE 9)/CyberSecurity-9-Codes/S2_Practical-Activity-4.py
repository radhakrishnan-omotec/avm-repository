import random
import string



def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(chars) for _ in range(length))
    return password



length = int(input("How long should the password be? (min 8): "))


if length < 8:
    print("❌ Password too short!")
else:
    print("🎯 Suggested Strong Password:", generate_password(length))