import sys
import os
sys.path.append(os.path.abspath('Database'))
sys.path.append(os.path.abspath('Errors'))
from database import DatabaseManager
from RegistationError import *
from Utils.VerificaitionUtil import HasEmptyFields
from psycopg2.errors import UniqueViolation

class RegisterStudentModel:
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
            db.InsertStudent(id, name, surname, birthday, phone, email)
            self._message = 'Student successfully registrated'
            self._isRegistrated = True
        except UniqueIdViolation as e:
            self._isRegistrated = False
            self._message = e.message
        except UniqueEmailViolation as e:
            self._isRegistrated = False
            self._message = e.message
        except UniquePhoneViolation as e:
            self._isRegistrated = False
            self._message = e.message 
        except EmptyFieldError as e:
            self._isRegistrated = False
            self._message = e.message
        self.Notify()

