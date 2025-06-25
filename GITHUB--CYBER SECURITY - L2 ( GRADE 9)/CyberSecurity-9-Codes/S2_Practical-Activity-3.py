common_words = ["password", "123456", "qwerty", "letmein", "admin", "welcome"]



def is_dictionary_based(password):
    return password.lower() in common_words



password = input("Enter a password: ")


if is_dictionary_based(password):
    print("❌ Weak! Your password is in the common dictionary.")
else:
    print("✅ Good! It's not a known dictionary word.")