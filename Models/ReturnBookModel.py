
import sys
import os
sys.path.append(os.path.abspath('Database'))
sys.path.append(os.path.abspath('Errors'))
from Database.database import DatabaseManager
from DeleteBookErrors import NonExistentBook

class ReturnBookModel:
    def __init__(self):
        pass

    def ReturnBook(self, idCopy):
        db = DatabaseManager()
        res = db.GetCopyState(idCopy)
        if (res is None):
            raise NonExistentBook("Entered copy doesn't exist.")
        else:
            print(res[0])
            if res[0] == 1:
                raise NonExistentBook("Book is available. Can't be returned to the library")
            else:
                res = db.UpdateCopyStateToAvailable(idCopy)
        db.DeleteStudentIssue(idCopy)
        db.CommitChanges()