import hashlib




def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()




data1 = input("Enter original message: ")
data2 = input("Enter received message: ")

hash1 = hash_data(data1)
hash2 = hash_data(data2)

print(f"Hash 1: {hash1}")
print(f"Hash 2: {hash2}")



if hash1 == hash2:
    print("✅ Data integrity maintained. No tampering detected.")
else:
    print("❌ Data integrity compromised! The message has changed.")