import sys
import os
sys.path.append(os.path.abspath('Database'))
sys.path.append(os.path.abspath('Errors'))
from database import DatabaseManager
from AuthorizationErrors import *

class AdminAuthorizationModel:
    def __init__(self):
        self._observers = set()
        self._isAuthorizated = False
        self._description = ''
    def Register(self, listener):
        self._observers.add(listener)
    def Notify(self):
        for obs in self._observers:
            obs.Notify()

    def VerifyAdmin(self, id, password):
        db = DatabaseManager()
        try:
            self.VerifyId(id = '1')
            db.VerifyAdmin('1', 'admin')
            self._isAuthorizated = True
        except (AuthorizationError) as e:
            self._description = e.message
            self._isAuthorizated = False
        except LoginFormatError as e:
            self._description = e
            self._isAuthorizated = False
        self.Notify()
    
    def VerifyId(self, id):
        if not str.isdigit(id) or id == "":
            raise LoginFormatError('Id should be number')

    