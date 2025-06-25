common_passwords = {"123456", "password", "qwerty", "abc123", "letmein"}




def is_weak_or_reused(user_passwords):
    unique_passwords = set()
    for pw in user_passwords:
        if pw in common_passwords or pw in unique_passwords:
            return True
        unique_passwords.add(pw)
    return False




# Simulated user password entries
employee_passwords = ["finance123", "password", "finance123"]

print("Reused or weak password detected?", is_weak_or_reused(employee_passwords))