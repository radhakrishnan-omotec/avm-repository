from datetime import datetime


log = []

def login(username, password):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    success = username == "user1" and password == "Secure!456"
    log.append(f"{timestamp} | User: {username} | {'Success' if success else 'Failed'}")
    return success
print("📝 Authentication Log Simulation")

for _ in range(3):
    uname = input("Username: ")
    pwd = input("Password: ")
    if login(uname, pwd):
        print("✅ Login successful.")
    else:
        print("❌ Login failed.")



print("\n🔍 Authentication Log:")
for entry in log:
    print(entry)
