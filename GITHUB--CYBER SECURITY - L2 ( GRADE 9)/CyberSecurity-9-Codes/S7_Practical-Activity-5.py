def ransomware_defense_checklist():
    checklist = {
        "Antivirus Installed": True,
        "System Up-to-Date": True,
        "Regular Backups": False,
        "MFA Enabled": True,
        "Avoids Suspicious Links": False
    }


    for item, status in checklist.items():
        icon = "✅" if status else "❌"
        print(f"{icon} {item}")



ransomware_defense_checklist()