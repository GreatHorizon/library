from Database.database import DatabaseManager
import sys
import os
sys.path.append(os.path.abspath('Errors'))
from FormatErrors import *
from IssuanceErrors import *

class EditBookModel():
    def __init__(self):
        pass

    def GetAuthorList(self, text):
        db = DatabaseManager()
        authorsArrayOfTuples = db.GetAuthorList(text)
        authorsArrayOfStrings = []
        for item in authorsArrayOfTuples:
            authorsArrayOfStrings.append(str(item[0]))
        return authorsArrayOfStrings    

    def GetAuthorBooksByName(self, authorName):
        db = DatabaseManager()
        booksTuples = db.GetAuthorBooks(authorName)
        booksArray = []
        for item in booksTuples:
            booksArray.append(str(item[0]))
        return booksArray

    def EditBook(self, newAuthorName, oldAuthorName, newBookName, oldBookName):
        CheckEmptyFields(newAuthorName, oldAuthorName, newBookName, oldBookName)
        db = DatabaseManager()
        if db.GetAuthorByName(oldAuthorName) is None:
            raise NonExistentAuthor("Author doesn't exists")
        if (newAuthorName == oldAuthorName):
            if (newBookName != oldBookName):
                idAuthor = db.GetAuthorByName(oldAuthorName)
                idBook = db.GetIdBookByNameAndAuthorId(oldBookName, idAuthor[0])
                db.UpdateAuthorBookName(idBook[0], newBookName)
                db.CommitChanges()
        else:
            existingAuthor = db.GetAuthorByName(newAuthorName)
            print(existingAuthor)
            if not existingAuthor:
                newAuthorId = db.InsertNewAuthor(newAuthorName)
                oldAuthorId = db.GetAuthorByName(oldAuthorName)
                idBook = db.GetIdBookByNameAndAuthorId(oldBookName, oldAuthorId[0])
                if (newBookName != oldBookName):
                    db.UpdateBookNameById(newBookName, idBook[0])
                db.DeleteBookFromOldAuthor(oldAuthorId[0], idBook[0])
                db.InsertBookToAuthor(idBook[0], newAuthorId[0])
                db.CommitChanges()
            else:
                oldAuthorId = db.GetAuthorByName(oldAuthorName) 
                idBook = db.GetIdBookByNameAndAuthorId(oldBookName, oldAuthorId[0])
                if (newBookName != oldBookName):
                    db.UpdateBookNameById(newBookName, idBook[0])
                db.UpdateAuthorBook(existingAuthor[0], idBook[0], oldAuthorId[0])
                db.CommitChanges()


def CheckEmptyFields(newAuthorName, oldAuthorName, newBookName, oldBookName):
    pass