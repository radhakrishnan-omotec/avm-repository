import subprocess




def scan_wifi_networks():
    print("📶 Scanning for nearby Wi-Fi networks...\n")
    result = subprocess.run(["nmcli", "-f", "SSID,SIGNAL", "dev", "wifi"], capture_output=True, text=True)
    print(result.stdout)



scan_wifi_networks()