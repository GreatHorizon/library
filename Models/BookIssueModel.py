import sys
import os
sys.path.append(os.path.abspath('Database'))
sys.path.append(os.path.abspath('Errors'))
from database import DatabaseManager

class BookIssueModel:
    def __init__(self):
        self._observers = set()

    
    def GetStudentsList(self):
        db = DatabaseManager()
        stArrayOfTuples = db.GetStudentsId()
        stArrayOfStrings = []
        for item in stArrayOfTuples:
            stArrayOfStrings.append(str(item[0]))
        return stArrayOfStrings

    def GetAuthorList(self):
        db = DatabaseManager()
        authorsArrayOfTuples = db.GetAuthorList()
        authorsArrayOfStrings = []
        for item in authorsArrayOfTuples:
            authorsArrayOfStrings.append(str(item[0]))
        return authorsArrayOfStrings