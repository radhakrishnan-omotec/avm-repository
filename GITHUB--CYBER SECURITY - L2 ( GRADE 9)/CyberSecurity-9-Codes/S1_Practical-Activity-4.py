import uuid



def authenticate_user(username, password):
    if username == "admin" and password == "admin123":
        return str(uuid.uuid4())
    return None


print("🔑 Token-Based Authentication")
user = input("Username: ")
pwd = input("Password: ")


token = authenticate_user(user, pwd)


if token:
    print(f"✅ Login successful! Your session token is: {token}")
    print("Use this token to access further resources securely.")
else:
    print("❌ Authentication failed.")
