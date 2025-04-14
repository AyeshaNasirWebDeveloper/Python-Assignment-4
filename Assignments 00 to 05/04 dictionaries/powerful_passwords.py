from hashlib import sha256

def check_login(user_email, saved_accounts, password_input):
    """
    Checks if the password entered matches the saved (hashed) password for the given email.
    
    Args:
        user_email (str): Email entered by the user.
        saved_accounts (dict): Dictionary with email as key and hashed password as value.
        password_input (str): Password to verify.
        
    Returns:
        bool: True if password is correct, False otherwise.
    """
    hashed_input = hash_password(password_input)
    return saved_accounts.get(user_email) == hashed_input

def hash_password(password):
    """
    Hashes the password using SHA256 and returns the hexadecimal string.
    
    Args:
        password (str): The password to hash.
        
    Returns:
        str: SHA256 hash of the password.
    """
    return sha256(password.encode()).hexdigest()

def main():
    # A sample database of email-password pairs (hashed)
    account_data = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # password
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # Karel
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # 123!456?789
    }

    print(check_login("example@gmail.com", account_data, "word"))         # False
    print(check_login("example@gmail.com", account_data, "password"))     # True

    print(check_login("code_in_placer@cip.org", account_data, "Karel"))   # True
    print(check_login("code_in_placer@cip.org", account_data, "karel"))   # False

    print(check_login("student@stanford.edu", account_data, "password"))  # False
    print(check_login("student@stanford.edu", account_data, "123!456?789"))  # True

if __name__ == '__main__':
    main()
