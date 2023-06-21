from cryptography.fernet import Fernet
import configparser


def get_linkedinpassword():
    config = configparser.ConfigParser()
    config.read("config.ini")
    key = b'7D7DHESYe95IyfUzTkyp7P1SZ5l7yi1gLMgkj0Hu5y8='
    encrypted_linkedinpassword = config.get("Passwords", "linkedin_password")
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_linkedinpassword.encode()).decode()
    return decrypted_password


def get_emailpassword():
    config = configparser.ConfigParser()
    config.read("config.ini")
    key = b'7D7DHESYe95IyfUzTkyp7P1SZ5l7yi1gLMgkj0Hu5y8='
    encrypted_emailpassword = config.get("Passwords", "email_password")
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_emailpassword.encode()).decode()
    return decrypted_password
