
import sys
import os
sys.path.append(os.path.abspath('Errors'))
from FormatErrors import *
from IssuanceErrors import *
from Models.AdminPageModel import AdminPageModel
from psycopg2.errors import *

class EditBookController():
    def __init__(self, master, model, view):
        self._master = master
        self._model = model
        self._view = view

    def EditBook(self, newAuthorName, oldAuthorName, newBookName, oldBookName):
        try:
            self._model.EditBook(newAuthorName, oldAuthorName, newBookName, oldBookName)
            self._view.ClearAllFieldsTab1()
            self._view.SetMessageLabelTab1("Book successfully edited", 'green')
        except NonExistentAuthor as e:
            self._view.SetMessageLabelTab1(e.message, 'red')
        except EmptyFieldError as e:
            self._view.SetMessageLabelTab1(e.message, 'red')
        except Exception:
            self._view.SetMessageLabelTab1("Unexpected error", 'red')

    def GetAuthors(self, text):
        booksList = self._model.GetAuthorList(text)
        return booksList

    def EnableBooksListTab1(self, authorName):
        if (not authorName):
            self._view.DisableBooksListTab1()
            self._view.ClearEntryFieldsTab1()
            self._view.DisableFieldsTab1()
            self._view.SetMessageLabelTab1('', 'white')
        else:
            booksList = self._model.GetAuthorBooksByName(authorName)
            if (len(booksList) == 0):
                self._view.DisableBooksListTab1()
                self._view.SetMessageLabelTab1("There are no books of this author in library. Try another book.", "red")
            else:
                self._view.EnableBooksListAndFillValuesTab1(booksList)



    def EnableNewNamesFieldsWithValues(self, authorName, bookName):
        self._view.EnableNewAuthorNameEntryWithTextTab1(authorName)
        self._view.EnableNewBookNameEntryWithTextTab1(bookName)

    def EnableBooksListTab2(self, authorName):
        if (not authorName):
            self._view.DisableBooksListTab2()
            self._view.DisableCopiesListTab2()
            self._view.ClearEntryFieldsTab2()
            self._view.DisableFieldsTab1()
            self._view.SetMessageLabelTab2('', 'white')
        else:
            booksList = self._model.GetAuthorBooksByName(authorName)
            if (len(booksList) == 0):
                self._view.DisableBooksListTab2()
                self._view.SetMessageLabelTab2("There are no books of this author in library. Try another book.", "red")
            else:
                self._view.EnableBooksListAndFillValuesTab2(booksList)


    def EnableCopiesListTab2(self, event):
        self._view.SetMessageLabelTab2('', 'white')
        copies = self._model.GetBookCopies(event.widget.get())
        if (len(copies) == 0):
            self._view.DisableCopiesListTab2()
            self._view.SetMessageLabelTab2("There are no copies in library. Try another copy.", "red")
        else:
            self._view.EnableCopiesListAndFillValuesTab2(copies)

    def GetCopyInfo(self, event):     
        info = self._model.GetCopyInfo(event.widget.get())
        self._view.EnableNewPagesEntryTab2(info[0])
        self._view.EnableNewPublisherNameEntryTab2(info[1])

    def EditBookCopy(self, idCopy, newPagesCount, newPublisherName):
        try:
            self._model.ChangeBookCopyInfo(idCopy, newPagesCount, newPublisherName)
            self._view.ClearAllFieldsTab2()
            self._view.SetMessageLabelTab2("Book copy successfully edited", 'green')
        except EmptyFieldError as e:
            self._view.SetMessageLabelTab2(e.message, 'red')
        except InvalidTextRepresentation:
            self._view.SetMessageLabelTab2("New page count should be number", 'red')
        except Exception as e:
            print(e)
            self._view.SetMessageLabelTab2("Unexpected error", "red")


    def BackToAdminPage(self):
        from Views.AdminPage import AdminPage
        self._master.switch_frame(AdminPage, AdminPageModel)



    