
import sys
import os
sys.path.append(os.path.abspath('Errors'))
from FormatErrors import *
from IssuanceErrors import *
from Models.AdminPageModel import AdminPageModel

class EditBookController():
    def __init__(self, master, model, view):
        self._master = master
        self._model = model
        self._view = view

    def EditBook(self, newAuthorName, oldAuthorName, newBookName, oldBookName):
        try:
            self._model.EditBook(newAuthorName, oldAuthorName, newBookName, oldBookName)
            self._view.ClearAllFields()
            self._view.SetMessageLabel("Book successfully edited", 'green')
        except NonExistentAuthor as e:
            self._view.SetMessageLabel(e.message, 'red')
        except EmptyFieldError as e:
            self._view.SetMessageLabel(e.message, 'red')
        except Exception:
            self._view.SetMessageLabel("Unexpected error", 'red')

    def GetAuthors(self, text):
        booksList = self._model.GetAuthorList(text)
        return booksList

    def EnableBooksList(self, authorName):
        if (not authorName):
            self._view.DisableBooksList()
            self._view.ClearEntryFields()
            self._view.DisableFields()
            self._view.SetMessageLabel('', 'white')
        else:
            booksList = self._model.GetAuthorBooksByName(authorName)
            if (len(booksList) == 0):
                self._view.DisableBooksList()
                self._view.SetMessageLabel("There are no books of this author in library. Try another book.", "red")
            else:
                self._view.EnableBooksListAndFillValues(booksList)

    def EnableNewNamesFieldsWithValues(self, authorName, bookName):
        self._view.EnableNewAuthorNameEntryWithText(authorName)
        self._view.EnableNewBookNameEntryWithText(bookName)



    def BackToAdminPage(self):
        from Views.AdminPage import AdminPage
        self._master.switch_frame(AdminPage, AdminPageModel)
    