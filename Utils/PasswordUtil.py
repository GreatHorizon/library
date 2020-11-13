import hashlib
import os

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

# new = GenerateEncodedPassword("admin")
# print(new.decode("utf-16"))
# salt = new[:32]
# res = GetEncodedPassword("admin", salt)
# print(new[32:])
# print("------------------------")
# print(res)

# def test_PYTHONPATH():
#   print("path is: ", os.environ.get('PYTHONPATH'))

# test_PYTHONPATH()