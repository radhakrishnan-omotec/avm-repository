from Crypto.Cipher import AES
import hashlib
import base64





def pad(msg): return msg + (16 - len(msg) % 16) * ' '



key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_ECB)


data = input("Enter data to store securely: ")
encrypted = cipher.encrypt(pad(data).encode())
hash_val = hashlib.sha256(data.encode()).hexdigest()



# Store encrypted + hash
print("\n📝 Data stored securely:")
print("Encrypted (base64):", base64.b64encode(encrypted).decode())
print("SHA-256 Hash:", hash_val)