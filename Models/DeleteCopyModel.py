
from Database.database import DatabaseManager
from AuthorizationErrors import *

class DeleteCopyModel:
    def __init__(self):
        self._observers = set()
        self._isDeleted = False
        self._message = ''

    def Register(self, listener):
        self._observers.add(listener)

    def Notify(self):
        for obs in self._observers:
            obs.Notify()

    def DeleteCopy(self, copyId):
        if (copyId and copyId.isnumeric()) :
            try:
                db = DatabaseManager()
                db.DeleteCopy(copyId)
                self._message = "Book successfully removed"
                self._isDeleted = True
            except NonExistentBook as e:
                self._message = e.message
                self._isDeleted = False
        else: 
            self._message = "Book id should be numeric string"
            self._isDeleted = False
        
        self.Notify()
