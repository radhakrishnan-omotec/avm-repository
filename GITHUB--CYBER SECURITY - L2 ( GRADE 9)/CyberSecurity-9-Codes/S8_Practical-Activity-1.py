def dns_spoof_sim(domain):
    fake_dns = {
        "www.bank.com": "192.0.2.66",  # Malicious IP
        "www.mail.com": "203.0.113.1"
    }

    real_dns = {
        "www.bank.com": "142.251.32.110",
        "www.mail.com": "172.217.11.101"
    }


    spoofed_ip = fake_dns.get(domain)
    original_ip = real_dns.get(domain)



    print(f"🌐 Domain: {domain}")
    print(f"🛡️ Legitimate IP: {original_ip}")
    print(f"⚠️ Spoofed IP Redirect: {spoofed_ip}")
    print("🚨 You have been redirected! Possible DNS Spoofing attack!")




dns_spoof_sim("www.bank.com")