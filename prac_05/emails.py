"""
Email to name
Estimate: 40 minutes
Actual:   35 minutes
"""

def get_name_from_email(email):
    """Get name from email address."""
    username = email.split('@')[0]
    name_parts = username.replace('_', '.').split('.')
    name = " ".join(name_parts).title()
    return name

email_to_name = {}
email = input("Email: ")
while email != "":
    name = get_name_from_email(email)
    confirmation = input(f"Is your name {name}? (Y/n) ")
    if confirmation.upper() != "Y" and confirmation != "":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print(f"{name} ({email})")
