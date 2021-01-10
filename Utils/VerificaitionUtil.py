import sys
import os
sys.path.append(os.path.abspath('Errors'))
from FormatErrors import *
import re

def IsEmpty(str):
    return not str

def IsNumber(id):
    if not str.isdigit(id) or id == "":
        raise InvalidFormatForDigit('Not number')


def ValidateEmail(email):
    emailreg = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if (emailreg.match(email) is None):
        raise BaseFormatError('Incorrect email format')

def ValidatePhone(phone):
    """
    Validation samples:     
        +7(903)888-88-88
        8(999)99-999-99
        +380(67)777-7-777
        001-541-754-3010
        +1-541-754-3010
        19-49-89-636-48018
        +233 205599853
    """
    phonereg = re.compile(r'^(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){10,14}(\s*)?$')
    if (phonereg.match(phone) is None):
        raise BaseFormatError('Incorrect phone format')
