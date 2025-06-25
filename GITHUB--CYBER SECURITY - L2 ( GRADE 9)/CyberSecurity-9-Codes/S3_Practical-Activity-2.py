import time
import hashlib




def generate_totp(secret, interval=30):
    counter = int(time.time()) // interval
    return hashlib.sha1(f"{secret}{counter}".encode()).hexdigest()[:6]




shared_secret = "SecretKey123"
print("⏳ TOTP Generator (Time-based OTP)")
otp = generate_totp(shared_secret)

print(f"Your current OTP is: {otp}")
input("Enter the OTP shown: ")
print("✅ Verification Passed (Simulated)")