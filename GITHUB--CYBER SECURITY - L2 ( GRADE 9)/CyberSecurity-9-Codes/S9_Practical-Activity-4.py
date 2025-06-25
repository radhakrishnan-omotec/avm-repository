users = {
    "user1": {"mfa": True, "role": "Admin"},
    "user2": {"mfa": False, "role": "Finance"},
    "user3": {"mfa": True, "role": "Support"}
}



def find_vulnerable_users(users_dict):
    return [user for user, config in users_dict.items() if not config["mfa"]]




print("Users without MFA:", find_vulnerable_users(users))