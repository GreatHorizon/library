import sys
import os
from Database.database import DatabaseManager
sys.path.append(os.path.abspath('Errors'))
sys.path.append(os.path.abspath('Utils'))
from AuthorizationErrors import *
from VerificaitionUtil import *
from Models.AbstractModel import AbstractModel

class ChangeStudentPasswordModel(AbstractModel):
    def __init__(self):
        self._observers = set()
        self._isChanged= False
        self._message = ''
        self._studentId = int()

    def Save(self, data):
        self._studentId = data[0]

    def Register(self, listener):
        self._observers.add(listener)

    def Notify(self):
        for obs in self._observers:
            obs.Notify()  

    def SetNewPassword(self, old, new, conf):
        db = DatabaseManager()
        try:
            db.CheckOldPassword(self._studentId, old)
            IsEqualsPasswords(new, conf)
            IsCorrectPasswordLength(conf)
            db.UpdatePassword(self._studentId, new)
            self._isChanged = True
            self._message = "Password changed successfully"
        except IncorrectPassword as e:
            self._message = e.message
            self._isChanged = False
        except NotEqualsPasswords as e:
            self._message = e.message
            self._isChanged = False
        self.Notify()


def IsCorrectPasswordLength(pswrd):
    if (len(pswrd) < 6):
        raise IncorrectPassword("New password length should be greater than 6 symbols")

def IsEqualsPasswords(password1, password2):
    if (password1 != password2):
        raise NotEqualsPasswords("Passwords aren't equals")