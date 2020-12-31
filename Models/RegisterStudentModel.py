import sys
import os
sys.path.append(os.path.abspath('Database'))
sys.path.append(os.path.abspath('Errors'))
from database import DatabaseManager
from FormatErrors import *
from RegistationError import *
from Models.AbstractModel import AbstractModel
from Utils.VerificaitionUtil import *
import re

class RegisterStudentModel(AbstractModel):
    def __init__(self):
        self._isRegistrated = False
        self._message = ''
        self._observers = set()

    def Register(self, listener):
        self._observers.add(listener)

    def Notify(self):
        for obs in self._observers:
            obs.Notify()
        
    def RegisterNewStudent(self, id, name, surname, birthday, phone, email):
        db = DatabaseManager()
        try:
            HasEmptyFields(id, name, surname, birthday, phone, email)
            IsNumber(id)
            ValidatePhone(phone)
            ValidateEmail(email)
            db.InsertStudent(id, name, surname, birthday, phone, email)
            self._message = 'Student successfully registrated'
            self._isRegistrated = True
        except BaseUniqueViolation as e:
            self._isRegistrated = False
            self._message = e.message
        except InvalidFormatForDigit:
            self._isRegistrated = False
            self._message = "Student id should be number"
        except BaseFormatError as e:
            self._isRegistrated = False
            self._message = e.message
        self.Notify()

def HasEmptyFields(id, name, surname, birthday, phone, email):
    if (IsEmpty(id)
        or IsEmpty(name)
        or IsEmpty(surname)
        or IsEmpty(birthday)
        or IsEmpty(phone)
        or IsEmpty(email)):
        raise EmptyFieldError("There are empty fields")

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


