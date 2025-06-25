import random




def generate_otp():
    return str(random.randint(100000, 999999))



correct_password = "CyberSecure123!"
print("🔐 Multi-Factor Authentication Simulation")


pwd = input("Enter your password: ")


if pwd == correct_password:
    otp = generate_otp()
    print(f"Your OTP is: {otp} (simulate this being sent to your phone)")
    entered_otp = input("Enter the OTP: ")
    if entered_otp == otp:
        print("✅ Access granted!")
    else:
        print("❌ Incorrect OTP. Access denied.")
else:
    print("❌ Wrong password. Access denied.")
