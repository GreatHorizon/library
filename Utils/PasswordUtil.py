import hashlib
import os
import psycopg2

def GenerateEncodedPassword(password):
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + key

def GetEncodedPassword(key, salt):
    new_key = hashlib.pbkdf2_hmac(
    'sha256',
    key.encode("utf-8"), # Конвертирование пароля в байты
    salt, 
    100000
    )
    return new_key

def GetSaltPart(encodedPassword):
    return encodedPassword[:32]

def GetPasswordPart(encodedPassword):
    return encodedPassword[32:]

