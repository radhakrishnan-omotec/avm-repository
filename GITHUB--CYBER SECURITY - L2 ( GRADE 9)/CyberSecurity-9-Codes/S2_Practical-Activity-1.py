import re



def analyze_password_strength(password):
    print("\n🔐 Password Strength Report:")
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*()_+]", password):
        score += 1
    if score == 5:
        print("✅ Excellent – Very Strong Password")
    elif score >= 3:
        print("⚠️ Moderate – Consider improving it")
    else:
        print("❌ Weak – Easy to crack")



password = input("Enter a password to check its strength: ")
analyze_password_strength(password)