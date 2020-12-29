import sys
import os
sys.path.append(os.path.abspath('Database'))
from database import DatabaseManager
from AuthorizationErrors import *
from Models.AbstractModel import AbstractModel

class StudentIssuanceModel(AbstractModel):
    def __init__(self):
        self._observers = set()
        self._isAuthorizated = False
        self._message = ''
        self._userId = int()

    def Save(self, data):
        self._userId = data[0]
        print(self._userId)
        
    def Register(self, listener):
        self._observers.add(listener)

    def Notify(self):
        for obs in self._observers:
            obs.Notify()

    def ParseTuple(self, tuple) :
        list = []
        for row in tuple:
            list.append(str(row))
        print(list, 'parse one tuple')
        return list

    def GetStudentIssuance(self, id):
        try:
            db = DatabaseManager()
            issuanceList = db.GetStudentIssuance(id)
            print(issuanceList)
            formatedList = []
            for issuance in issuanceList:
                formatedList.append(self.ParseTuple(issuance))
            return formatedList
        except NoIssuance as e:
            self._message = e.message
