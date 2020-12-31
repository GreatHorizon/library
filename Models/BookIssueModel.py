import sys
import os
sys.path.append(os.path.abspath('Database'))
sys.path.append(os.path.abspath('Errors'))
sys.path.append(os.path.abspath('Utils'))
from database import DatabaseManager
from FormatErrors import *
from IssuanceErrors import *
from Models.AbstractModel import AbstractModel
from VerificaitionUtil import *
import psycopg2

class BookIssueModel(AbstractModel):
    def __init__(self):
        self._observers = set()

    def GetStudentsList(self, text):
        db = DatabaseManager()
        stArrayOfTuples = db.GetStudentsInfoPart(text)
        stArrayOfStrings = []
        for item in stArrayOfTuples:
            stArrayOfStrings.append(str(item[0]))
        return stArrayOfStrings

    def GetAuthorList(self, text):
        db = DatabaseManager()
        authorsArrayOfTuples = db.GetAuthorList(text)
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
        CheckEmptyFields(studentId, author, book, copy, start, end)
        db = DatabaseManager()
        IsNumber(studentId)
        if db.GetStudentById(studentId) is None:
            raise NonExistentStudent("Student doesn't exists")
        if db.GetAuthorByName(author) is None:
            raise NonExistentAuthor("Author doesn't exists")
        try:
            db.UpdateCopyStateToUnavailable(copy)
            db.InsertIssuance(studentId, copy, start, end)
            db.CommitChanges() 
        except (Exception) as e:
            print(e)
            raise e



def CheckEmptyFields(studentId, author, book, copy, start, end):
    if(IsEmpty(studentId) or
        IsEmpty(author) or
        IsEmpty(book) or
        IsEmpty(copy) or
        IsEmpty(start) or
        IsEmpty(end)):
        raise EmptyFieldError('There are empty fields')
