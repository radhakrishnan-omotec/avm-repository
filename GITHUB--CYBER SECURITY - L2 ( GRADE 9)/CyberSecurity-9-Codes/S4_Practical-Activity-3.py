import time



print("📡 Simulating fake requests to a service...")

for i in range(1, 101):
    time.sleep(0.05)  # Simulate delay
    print(f"Request #{i}: Service under load...")



print("⚠️ Service temporarily unavailable due to high traffic!")