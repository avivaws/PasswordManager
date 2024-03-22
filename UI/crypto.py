import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def encrypt(password, message):
    password = bytes(password, 'utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=bytes([0] * 16),
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    return f.encrypt(bytes(message, 'utf-8'))


def decrypt(password, token):
    password = bytes(password, 'utf-8')
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=bytes([0] * 16),
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    try:
        return f.decrypt(token).decode('utf-8')
    except Exception as e:
        return None

# x='123456'
# password='xyz'
# enc=encrypt(password, x)
# print(enc)
# dec=decrypt(password, enc)
# print(dec)