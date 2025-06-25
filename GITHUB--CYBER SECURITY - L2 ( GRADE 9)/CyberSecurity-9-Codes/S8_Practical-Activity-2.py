def dns_tunneling_sim(data):
    print("📡 Simulating DNS tunneling of data...")

    encoded_data = '.'.join(format(ord(char), 'x') for char in data)
    dns_query = f"{encoded_data}.malicious-domain.com"

    print(f"🚨 Encoded Data in DNS Query: {dns_query}")




dns_tunneling_sim("topsecret")