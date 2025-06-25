def detect_fake_ssids(available_ssids):
    legitimate = "CompanyWiFi"
    flagged = []
    
    for ssid in available_ssids:
        if ssid.lower().replace(" ", "") != legitimate.lower():
            flagged.append(ssid)

    return flagged




# Usage SSID list
ssids = ["CompanyWiFi", "CompnyWiFi", "Company Wifi", "CompanyWiFi_Free"]
suspicious = detect_fake_ssids(ssids)

print("⚠️ Suspicious SSIDs detected:", suspicious)