def check_url_security(url):
    if url.startswith("https://"):
        print("✅ Secure connection detected.")
    elif url.startswith("http://"):
        print("❌ Insecure connection detected – vulnerable to SSL stripping!")
    else:
        print("❓ Unknown protocol.")




# Usage URLs
urls = ["https://bank.com", "http://bank-login.com"]
for u in urls:
    check_url_security(u)