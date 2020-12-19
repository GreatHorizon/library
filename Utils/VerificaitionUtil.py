import sys
import os
sys.path.append(os.path.abspath('Errors'))
from AuthorizationErrors import *
from RegistationError import *

def VerifyId(id):
    if not str.isdigit(id) or id == "":
        raise LoginFormatError('Id should be number')

def IsEmpty(str):
    return not str

def HasEmptyFields(id, name, surname, birthday, phone, email):
    if (IsEmpty(id)
        or IsEmpty(name)
        or IsEmpty(surname)
        or IsEmpty(birthday)
        or IsEmpty(phone)
        or IsEmpty(email)):
        raise EmptyFieldError("There are empty fields")

def IsEuqalsPasswords(password1, password2):
    if (password1 != password2):
        raise NotEqualsPasswords("Passwords aren't equals")