import sys
import os
sys.path.append(os.path.abspath('Database'))
sys.path.append(os.path.abspath('Errors'))
from database import DatabaseManager
from Models.AbstractModel import AbstractModel

class BookIssueModel(AbstractModel):
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

    def GetAuthorBooksByName(self, name):
        db = DatabaseManager()
        booksTuples = db.GetAuthorBooks(name)
        booksArray = []
        for item in booksTuples:
            booksArray.append(str(item[0]))
        return booksArray

    def GetBookCopies(self, name):
        db = DatabaseManager()
        copiesTuples = db.GetCopies(name)
        copiesArray = []
        for item in copiesTuples:
            copiesArray.append(str(item[0]))
        return copiesArray

    def CreateIssue(self, studentId, author, book, copy, start, end):
        print(studentId, author, book, copy, start, end)