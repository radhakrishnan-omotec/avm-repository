import re



def check_password_strength(password):
    print("\n🔐 Checking password strength...")
    if len(password) < 8:
        print("❌ Too short! Minimum 8 characters recommended.")
    elif not re.search("[A-Z]", password):
        print("❌ Add at least one uppercase letter.")
    elif not re.search("[0-9]", password):
        print("❌ Include at least one number.")
    elif not re.search("[!@#$%^&*()_+]", password):
        print("❌ Include at least one special character.")
    else:
        print("✅ Strong password!")



password = input("Enter your password to test: ")
check_password_strength(password)