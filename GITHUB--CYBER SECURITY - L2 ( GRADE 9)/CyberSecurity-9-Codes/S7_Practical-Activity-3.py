def detect_malicious_attachment(subject, attachment_name):
    if any(ext in attachment_name.lower() for ext in ['.exe', '.js', '.scr', '.zip']):
        print(f"📧 Email Subject: {subject}")
        print(f"📎 Attachment: {attachment_name}")
        print("⚠️ Malicious attachment suspected! Do not open unknown file types.")
    else:
        print("✅ Attachment appears safe.")





detect_malicious_attachment("Urgent Update Required", "update_patch.exe")