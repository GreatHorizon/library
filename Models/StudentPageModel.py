
import sys
import os
sys.path.append(os.path.abspath('Database'))
from database import DatabaseManager
from Models.AbstractModel import AbstractModel

class StudentPageModel(AbstractModel):
    def __init__(self):
        self._studentId = int()

    def Save(self, data):
        self._studentId = data[0]

    def GetStudentName(self):        
        db = DatabaseManager()
        res = db.GetStudentName(self._studentId)
        return res
        