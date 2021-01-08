import sys
import os
sys.path.append(os.path.abspath('Database'))
sys.path.append(os.path.abspath('Errors'))
from database import DatabaseManager
from Models.AbstractModel import AbstractModel

class StudentDebtsModel(AbstractModel):
    def __init__(self):
        self._idStudent = int()

     
    def GetStudentsList(self, text):
        db = DatabaseManager()
        stArrayOfTuples = db.GetStudentsInfoPart(text)
        stArrayOfStrings = []
        for item in stArrayOfTuples:
            stArrayOfStrings.append(str(item[0]))
        return stArrayOfStrings
    
    def GetStudentDebts(self, studentId):
        db = DatabaseManager()
        debtsArrayOfTuples = db.GetStudentIssuance(studentId)
        return debtsArrayOfTuples

    def ReturnBooks(self, idsArray):
        db = DatabaseManager()
        for id in idsArray:
            db.UpdateCopyStateToAvailable(id)
            db.DeleteStudentIssue(id)
            db.CommitChanges()

    def GetStudentInfo(self, id):
        db = DatabaseManager()
        info = db.GetStudentInfoById(id)
        return info

    def GetStudentId(self, idCopy):
        db = DatabaseManager()
        res = db.GetStudentIdByIssuedCopyId(idCopy)
        return res[0]