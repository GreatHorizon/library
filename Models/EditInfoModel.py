
import sys
import os
sys.path.append(os.path.abspath('Database'))
from database import DatabaseManager
from Models.AbstractModel import AbstractModel
from Utils.VerificaitionUtil import ValidateEmail, ValidatePhone
from FormatErrors import *

class EditInfoModel(AbstractModel):
    def __init__(self):
        self._observers = set()
        self._studentId = int()
    
    def Save(self, data):
        self._studentId = data[0]

    def Register(self, listener):
        self._observers.add(listener)

    def Notify(self):
        for obs in self._observers:
            obs.Notify()  

    def GetStudentInfo(self):        
        db = DatabaseManager()
        res = db.GetStudentInfo(self._studentId)
        return res

    def ChangeInfo(self, newEmail, newPhone):
        if (newEmail == '' and newPhone == ''):
            raise EmptyFieldError('At least one of filled should be filled')

        db = DatabaseManager()

        if(newPhone != '') :
            ValidatePhone(newPhone)
            db.UpdatePhone(self._studentId, newPhone)

        if(newEmail != '') :
            ValidateEmail(newEmail)
            db.UpdateEmail(self._studentId, newEmail)
        
    