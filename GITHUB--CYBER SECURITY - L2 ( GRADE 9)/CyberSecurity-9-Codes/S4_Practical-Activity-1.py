from Crypto.Cipher import AES
import base64




def pad(text):
    return text + (16 - len(text) % 16) * ' '



key = b'Sixteen byte key'
cipher = AES.new(key, AES.MODE_ECB)


message = input("Enter a message to encrypt: ")
padded_msg = pad(message)
ciphertext = cipher.encrypt(padded_msg.encode())
encoded = base64.b64encode(ciphertext).decode()



print(f"🔒 Encrypted Message: {encoded}")


# Decryption
decoded = base64.b64decode(encoded)
plaintext = cipher.decrypt(decoded).decode().strip()

print(f"🔓 Decrypted Message: {plaintext}")