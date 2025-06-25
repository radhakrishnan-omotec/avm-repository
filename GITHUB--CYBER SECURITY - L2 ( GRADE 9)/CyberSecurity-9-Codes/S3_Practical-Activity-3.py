stored_fingerprints = {
    "student1": "A1B2C3D4",
    "admin": "F5G6H7I8"
}



print("🧬 Biometric Authentication (Fingerprint) Simulator")
user = input("Username: ")
scan = input("Enter fingerprint hash (simulate): ")




if stored_fingerprints.get(user) == scan:
    print("✅ Fingerprint match! Identity confirmed.")
else:
    print("❌ Authentication failed. Fingerprint does not match.")