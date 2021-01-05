import sys
import os
sys.path.append(os.path.abspath('Database'))
sys.path.append(os.path.abspath('Errors'))
from database import DatabaseManager
from Models.AbstractModel import AbstractModel

class StudentDebtsModel(AbstractModel):
    def __init__(self):
        pass

     
    def GetStudentsList(self, text):
        db = DatabaseManager()
        stArrayOfTuples = db.GetStudentsInfoPart(text)
        stArrayOfStrings = []
        for item in stArrayOfTuples:
            stArrayOfStrings.append(str(item[0]))
        return stArrayOfStrings
    
    def ParseTuple(self, tuple):
        list = []
        for row in tuple:
            list.append(str(row))
        print(list, 'parse one tuple')
        return list

    def GetStudentDebts(self, studentId):
        db = DatabaseManager()
        debtsArrayOfTuples = db.GetStudentIssuance(studentId)
        print(debtsArrayOfTuples)
        formatedList = []
        for issuance in debtsArrayOfTuples:
            formatedList.append(self.ParseTuple(issuance))
        print(formatedList)
        return formatedList