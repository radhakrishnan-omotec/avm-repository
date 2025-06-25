import math



def time_to_crack(length, charset_size):
    attempts = charset_size ** length
    guesses_per_sec = 1000000000  # 1 billion guesses/second (modern GPUs)
    seconds = attempts / guesses_per_sec
    years = seconds / (60 * 60 * 24 * 365)
    return years




print("🔐 Brute Force Attack Simulation")

length = int(input("Enter the length of your password: "))
charset_size = int(input("Enter estimated charset size (26=letters, 52=upper+lower, 62+specials=95): "))
years = time_to_crack(length, charset_size)

print(f"⏳ Estimated time to crack: {years:.2f} years")