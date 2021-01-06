import sys
import os
sys.path.append(os.path.abspath('Database'))
sys.path.append(os.path.abspath('Errors'))
from database import DatabaseManager
from Models.AbstractModel import AbstractModel

class BookSearchModel(AbstractModel):
    def __init__(self):
        self._observers = set()
        self._searchStrategy = self.SearchByBookNameStrategy
        self._showStrategy = self.ShowByBookNameStrategy

    def Save(self, data):
        self._studentId = data[0]
        
    def Register(self, listener):
        self._observers.add(listener)

    def Notify(self):
        for obs in self._observers:
            obs.Notify()

    def SearchByAuthorStrategy(self, searchData=None) : 
        db = DatabaseManager()
        authorsArrayOfTuples = db.GetAuthorList(searchData)
        authorsArrayOfStrings = []
        for item in authorsArrayOfTuples:
            authorsArrayOfStrings.append(str(item[0]))
        return authorsArrayOfStrings
    
    def SearchByBookNameStrategy(self, searchData=None) : 
        db = DatabaseManager()
        booksArrayOfTuples = db.GetBooksList(searchData)
        booksArrayOfStrings = []
        for item in booksArrayOfTuples:
            booksArrayOfStrings.append(str(item[0]))
        return booksArrayOfStrings
    
    def ShowByBookNameStrategy(self, searchData=None) :
        db = DatabaseManager()
        return db.SearchBooksByName(searchData)

    def ShowByAuthorNameStrategy(self, searchData=None):
        db = DatabaseManager()
        array =  db.SearchBooksByAuthor(searchData)
        return array
