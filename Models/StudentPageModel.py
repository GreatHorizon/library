
import sys
import os
sys.path.append(os.path.abspath('Database'))
from database import DatabaseManager
from Models.AbstractModel import IModel

class StudentPageModel(IModel):
    def __init__(self):
        self._studentId = int()

    def Save(self, data):
        self._studentId = data[0]

    def GetStudentInfo(self):        
        db = DatabaseManager()
        res = db.GetStudentInfo(self._studentId)
        return res
        