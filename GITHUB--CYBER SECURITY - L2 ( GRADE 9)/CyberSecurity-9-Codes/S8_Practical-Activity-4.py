def resolve_with_spoof_check(domain, response_ip):
    known_legit_dns = {
        "example.com": "93.184.216.34",
        "securebank.com": "104.244.42.65"
    }


    real_ip = known_legit_dns.get(domain)
    if not real_ip:
        print(f"🔎 No reference IP available for {domain}.")
        return

    if response_ip != real_ip:
        print(f"🚨 WARNING: Spoofed response detected for {domain}!")
    else:
        print(f"✅ Safe: IP matches expected value for {domain}.")




resolve_with_spoof_check("securebank.com", "91.198.174.192")