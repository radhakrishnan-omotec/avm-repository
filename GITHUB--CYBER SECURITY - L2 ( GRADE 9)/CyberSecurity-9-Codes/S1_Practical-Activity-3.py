stored_fingerprints = {
    "student1": "ABC123XYZ",
    "student2": "JHG456QWE",
}



print("🧬 Biometric Authentication Simulator")
username = input("Enter username: ")
fingerprint = input("Scan fingerprint (enter hash string): ")



if username in stored_fingerprints and stored_fingerprints[username] == fingerprint:
    print("✅ Biometric Match! Access Granted.")
else:
    print("❌ Biometric Mismatch. Access Denied.")
