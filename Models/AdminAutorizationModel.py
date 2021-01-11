import sys
import os
sys.path.append(os.path.abspath('Database'))
sys.path.append(os.path.abspath('Errors'))
from database import DatabaseManager
from AuthorizationErrors import *
from Models.AbstractModel import IModel
from FormatErrors import InvalidFormatForDigit
from Utils.VerificaitionUtil import IsNumber

class AdminAuthorizationModel(IModel):
    def __init__(self):
        self._observers = set()
        self._isAuthorizated = False
        self._message = ''

    def Register(self, listener):
        self._observers.add(listener)

    def Notify(self):
        for obs in self._observers:
            obs.Notify()

    def VerifyAdmin(self, id, password):
        db = DatabaseManager()
        try:
            IsNumber(id)
            db.VerifyAdmin(id, password)
            self._isAuthorizated = True
        except AuthorizationError as e:
            self._message = e.message
            self._isAuthorizated = False
        except InvalidFormatForDigit as e:
            self._message = "Admin id should be number"
            self._isAuthorizated = False
        self.Notify()


    