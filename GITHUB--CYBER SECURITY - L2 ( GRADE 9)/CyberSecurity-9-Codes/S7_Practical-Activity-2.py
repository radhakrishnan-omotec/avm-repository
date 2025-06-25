def is_suspicious_file(filename):
    suspicious_ext = ['.exe', '.bat', '.vbs', '.scr']
    known_malware_names = ['ransom', 'keylogger', 'hacktool']
    
    for ext in suspicious_ext:
        if filename.endswith(ext):
            return True
    for name in known_malware_names:
        if name in filename.lower():
            return True
    return False




# Usage
files = ['setup.exe', 'resume.pdf', 'keylogger.scr']
suspicious = [f for f in files if is_suspicious_file(f)]


print("⚠️ Potential malware files detected:", suspicious)