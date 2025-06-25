import random



print("📲 SMS-Based Authentication")
phone_number = input("Enter your phone number: ")
print("Sending token...")


sms_code = str(random.randint(100000, 999999))
print(f"Simulated SMS Code: {sms_code}")



entered_code = input("Enter the code you received: ")


if entered_code == sms_code:
    print("✅ Access granted via SMS token.")
else:
    print("❌ Incorrect code.")