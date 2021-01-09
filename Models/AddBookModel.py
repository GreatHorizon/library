import sys
import os

from database import DatabaseManager
from AuthorizationErrors import *
from Models.AbstractModel import AbstractModel

class AddBookModel(AbstractModel):
    def __init__(self):
        self._observers = set()
        self._addedSuccessfuly = False
        self._description = ''

    def Register(self, listener):
        self._observers.add(listener)
    def Notify(self):
        for obs in self._observers:
            obs.Notify()

    def AddBook(self, isbn, bookName, author, pageCount, publisher):
        author = author.strip()
        bookName = bookName.strip()
        db = DatabaseManager()
        fieldsMap = {
            'isbn': isbn,
            'bookName': bookName,
            'author' : author,
            'pageCount' : pageCount,
            'publisher' : publisher
        }

        try:
            self.CheckFields(fieldsMap)
            idCopy = db.AddBook(isbn, bookName, author, pageCount, publisher)
            self._addedSuccessfuly = True
            self._description = "Book successfully added. Id copy = " + str(idCopy)
        except (FormatError) as e:
            self._description = e
            self._addedSuccessfuly = False
        except (AddBookError) as e:
            self._description = e
            self._addedSuccessfuly = False

        self.Notify()

    def CheckFields(self, fieldsMap):
        for key in fieldsMap:
            if not fieldsMap[key]:
                raise FormatError('All fields should be filled')
        
        if not str.isdigit(fieldsMap['isbn']) or (not len(fieldsMap['isbn']) == 10 and not len(fieldsMap['isbn']) == 13):
            raise FormatError('ISBN should be number with 10 or 13 digits')
        
        if not str.isdigit(fieldsMap['pageCount']):
            raise FormatError('Page count should be number')
        
        if int(fieldsMap['pageCount']) > 10000 :
            raise FormatError('Page count cant be more than 10000')

        
                