suspicious_keywords = ["urgent", "reset your password", "verify your account", "click here", "login", "limited time"]



def is_phishing(email_content):
    score = sum(1 for keyword in suspicious_keywords if keyword.lower() in email_content.lower())
    return score >= 2




# Simulated input
email = """
Hi, this is from HR. Please reset your password immediately to avoid suspension. Click here to proceed.
"""




print("Email flagged as phishing?" , is_phishing(email))