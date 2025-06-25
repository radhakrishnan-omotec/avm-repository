import random



def generate_otp():
    return str(random.randint(100000, 999999))



print("🔐 Multi-Factor Authentication (MFA) Demo")
username = input("Enter username: ")
password = input("Enter password: ")



if username == "student" and password == "MFAstrong!2024":
    otp = generate_otp()
    print(f"📲 Your OTP is: {otp} (simulated)")
    user_otp = input("Enter the OTP: ")
    if user_otp == otp:
        print("✅ MFA success! Access granted.")
    else:
        print("❌ Incorrect OTP.")
else:
    print("❌ Username or password incorrect.")