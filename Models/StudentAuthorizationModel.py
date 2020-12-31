import sys
import os
sys.path.append(os.path.abspath('Database'))
sys.path.append(os.path.abspath('Errors'))
from database import DatabaseManager
from AuthorizationErrors import *
from Models.AbstractModel import AbstractModel
from FormatErrors import InvalidFormatForDigit
from Utils.VerificaitionUtil import IsNumber


class StudentAuthorizationModel(AbstractModel):
    def __init__(self):
        self._observers = set()
        self._isAuthorizated = False
        self._message = ''
        self._userId = int()
        
    def Register(self, listener):
        self._observers.add(listener)

    def Notify(self):
        for obs in self._observers:
            obs.Notify()

    def VerifyStudent(self, id, password):
        db = DatabaseManager()
        try:
            IsNumber(id)
            db.VerifyStudent(id, password)
            self._isAuthorizated = True
            self._userId = id
        except AuthorizationError as e:
            self._message = e.message
            self._isAuthorizated = False
        except InvalidFormatForDigit as e:
            self._message = "Id student should be number"
            self._isAuthorizated = False
        self.Notify()


