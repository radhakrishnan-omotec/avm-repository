import re



def is_suspicious_link(url):
    suspicious_patterns = [r"bit\.ly", r"tinyurl\.com", r"login.*\.com", r"verify.*\.net"]
    for pattern in suspicious_patterns:
        if re.search(pattern, url):
            return True
    return False



# Usage
test_url = "http://bit.ly/verify-your-account"

if is_suspicious_link(test_url):
    print("⚠️ Suspicious link detected! Avoid clicking.")
else:
    print("✅ Link seems normal.")