import re

password_pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$])[A-Za-z\d!@#$]{8,}$"

def validate_password(password):
    if re.match(password_pattern, password):
        print("Valid password")
    else:
        print("Invalid password")

validate_password("Abc123!@#")