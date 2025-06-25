def simple_encrypt(text, key=3):
    return ''.join(chr((ord(c) + key) % 256) for c in text)




def simple_decrypt(encrypted, key=3):
    return ''.join(chr((ord(c) - key) % 256) for c in encrypted)




data = "Confidential Report"
locked = simple_encrypt(data)
unlocked = simple_decrypt(locked)



print("🔐 Encrypted:", locked)
print("🔓 Decrypted:", unlocked)