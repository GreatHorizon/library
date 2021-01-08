from  Models.AdminPageModel import AdminPageModel
import sys
import os
sys.path.append(os.path.abspath('Errors'))
from FormatErrors import BaseFormatError
from IssuanceErrors import *
from psycopg2.errors import *

class BookIssueController:
    def __init__(self, master, model, view):
        self._view = view
        self._master = master
        self._model = model

    def GetStudentsInfo(self, text):
        studentsList = self._model.GetStudentsList(text)
        print(studentsList)
        return studentsList
    
    def GetAuthors(self, text):
        booksList = self._model.GetAuthorList(text)
        return booksList

    # def GetAuthorsBookByName(self, name):
    #     booksList = self._model.GetAuthorBooksByName(name)
    #     print(booksList)

    def BackToAdminPage(self):
        from Views.AdminPage import AdminPage
        self._master.switch_frame(AdminPage, AdminPageModel)

    def EnableBooksList(self, authorName):
        if (not authorName):
            self._view.DisableBooksList()
            self._view.DisableCopiesList()
        booksList = self._model.GetAuthorBooksByName(authorName)
        if (len(booksList) == 0):
            self._view.DisableBooksList()
            self._view.SetErrorMessage("There are no books of this author in library. Try another book.")
        self._view.EnableBooksListAndFillValues(booksList)
        self._view.SetErrorMessage("")

    def EnableCopiesList(self, event):
        self._view.ClearMessageLabel()
        copies = self._model.GetBookCopies(event.widget.get())
        if (len(copies) == 0):
            self._view.DisableCopiesList()
            self._view.SetErrorMessage("There are no copies in library. Try another copy.")
        self._view.EnableCopiesListAndFillValues(copies)

    def CreateIssue(self, studentId, author, book, copy, start, end):
        try:
            self._model.CreateIssue(studentId, author, book, copy, start, end)
            self._view.SetSuccessMessage("Issue successfully created")
            self._view.ClearFields()
        except BaseIssuanceError as e:
            self._view.SetErrorMessage(e.message)
        except BaseFormatError as e:
            self._view.SetErrorMessage(e.message)
        except NumericValueOutOfRange:
            self._view.SetErrorMessage("Too big id student value")
        except Exception as e:
            print(e)
            self._view.SetErrorMessage("Unexpected Error")
