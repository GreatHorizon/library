import sys
import os
sys.path.append(os.path.abspath('Database'))
sys.path.append(os.path.abspath('Errors'))
from database import DatabaseManager
from AuthorizationErrors import *
from Utils.VerificaitionUtil import VerifyId
from Models.AbstractModel import AbstractModel

class AdminAuthorizationModel:
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
            VerifyId('1')
            db.VerifyAdmin('1', 'admin')
            self._isAuthorizated = True
        except (AuthorizationError) as e:
            self._message = e.message
            self._isAuthorizated = False
        except LoginFormatError as e:
            self._message = e
            self._isAuthorizated = False
        self.Notify()

    