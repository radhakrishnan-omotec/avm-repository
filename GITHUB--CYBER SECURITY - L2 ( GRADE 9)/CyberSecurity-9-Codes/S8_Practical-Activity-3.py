import random
import time




def simulate_ddos_attack(target, duration=5):
    print(f"🧨 Starting DDoS simulation on {target}...\n")
    end_time = time.time() + duration
    request_count = 0



    while time.time() < end_time:
        fake_ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
        print(f"🔁 Request from {fake_ip} → {target}")
        request_count += 1
        time.sleep(0.2)
    
    print(f"\n🔥 DDoS Simulation Ended: {request_count} requests sent in {duration} seconds.")




simulate_ddos_attack("www.victimsite.com", duration=3)