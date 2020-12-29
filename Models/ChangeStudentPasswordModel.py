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

    def Register(self, listener):
        self._observers.add(listener)

    def Notify(self):
        for obs in self._observers:
            obs.Notify()  

    def SetNewPassword(self, id, old, new, conf):
        db = DatabaseManager()
        try:
            db.UpdatePassword(id, old, new)
            IsEuqalsPasswords(new, conf)
            self._isChanged = True
            self._message = "Password changed successfully"
        except IncorrectPassword as e:
            self._message = e.message
            self._isChanged = False
        except NotEqualsPasswords as e:
            self._message = e.message
            self._isChanged = False
        self.Notify()