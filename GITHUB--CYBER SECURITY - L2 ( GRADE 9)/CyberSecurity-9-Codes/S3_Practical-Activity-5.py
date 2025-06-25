print("🔒 MFA Policy & Security Check")



mfa_enabled = input("Do you use MFA on your main email account? (yes/no): ").strip().lower()
strong_pass = input("Is your password at least 12 characters and includes symbols? (yes/no): ").strip().lower()
backup = input("Do you have a backup method like security questions or a hardware key? (yes/no): ").strip().lower()



score = sum([mfa_enabled == "yes", strong_pass == "yes", backup == "yes"])



if score == 3:
    print("✅ Great! You're well protected with strong MFA practices.")
elif score == 2:
    print("⚠️ Not bad, but there’s room for improvement.")
else:
    print("❌ Your account is at risk! Please update your security settings.")