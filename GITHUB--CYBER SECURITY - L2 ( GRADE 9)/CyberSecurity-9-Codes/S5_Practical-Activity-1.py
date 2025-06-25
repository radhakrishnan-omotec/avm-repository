def detect_phishing_email(subject, body):
    phishing_keywords = ['urgent', 'verify your account', 'password', 'login', 'click here', 'update', 'suspended']
    content = f"{subject} {body}".lower()

    for keyword in phishing_keywords:
        if keyword in content:
            return True
    return False




# Usage
subject = "Your account is suspended"
body = "Click here to verify your login credentials immediately."


if detect_phishing_email(subject, body):
    print("⚠️ Potential phishing email detected.")
else:
    print("✅ Email appears to be safe.")