import os
import time
import random



# Simulated file system structure
fake_files = [
    "Documents/report.docx",
    "Pictures/vacation.jpg",
    "Desktop/notes.txt",
    "Downloads/invoice.pdf",
    "Music/song.mp3"
]


def simulate_scan():
    print("🔍 Scanning your system for files...")
    time.sleep(1)
    for file in fake_files:
        print(f"📂 Found: {file}")
        time.sleep(0.5)

def simulate_encryption(files):
    print("\n🔐 Encrypting your files...")
    encrypted_files = []
    for file in files:
        enc_name = file.replace('.', '_ENCRYPTED.')
        encrypted_files.append(enc_name)
        print(f"🔒 {file} → {enc_name}")
        time.sleep(0.4)
    return encrypted_files

def simulate_ransomware():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("💻 RansomSim v2.0 - Educational Ransomware Simulator\n")
    simulate_scan()
    simulate_encryption(fake_files)

simulate_ransomware()