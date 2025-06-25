import random
import time


events = ["Phishing Email", "Port Scan", "Privilege Escalation", "Lateral Movement", "Data Exfiltration"]

blue_team_response = {
    "Phishing Email": "Blocked and Reported",
    "Port Scan": "Firewall Adjusted",
    "Privilege Escalation": "Account Locked",
    "Lateral Movement": "Segmented Network",
    "Data Exfiltration": "Isolated Server"
}



def simulate_red_blue():
    for _ in range(5):
        attack = random.choice(events)
        response = blue_team_response[attack]
        print(f"⚠️ Red Team Attack: {attack} | 🛡️ Blue Team Response: {response}")
        time.sleep(1)


simulate_red_blue()