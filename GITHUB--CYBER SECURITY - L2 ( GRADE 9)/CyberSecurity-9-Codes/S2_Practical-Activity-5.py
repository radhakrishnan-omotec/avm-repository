def validate_password(password):
    issues = []
    if len(password) < 10:
        issues.append("Password too short (minimum 10 characters).")
    if not re.search(r"[A-Z]", password):
        issues.append("Include at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        issues.append("Include at least one lowercase letter.")
    if not re.search(r"\d", password):
        issues.append("Include at least one digit.")
    if not re.search(r"[!@#$%^&*()_+=]", password):
        issues.append("Include at least one special character.")

        
    if issues:
        print("⚠️ Your password has the following issues:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("✅ Your password meets standard policy requirements!")




password = input("Enter a password to validate: ")
validate_password(password)