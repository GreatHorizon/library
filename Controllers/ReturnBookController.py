from Models.ReturnBookModel import ReturnBookModel
from Models.AdminPageModel import AdminPageModel
import sys
import os
sys.path.append(os.path.abspath('Errors'))
from DeleteBookErrors import NonExistentBook
from FormatErrors import BaseFormatError
from psycopg2.errors import *


class ReturnBookController:
    def __init__(self, master, model, view):
        self._view = view
        self._master = master
        self._model = model

    def BackToAdminPage(self):
        from Views.AdminPage import AdminPage
        self._master.switch_frame(AdminPage, AdminPageModel)

    def ReturnBook(self, idCopy):
        try:
            self._model.ReturnBook(idCopy)
            self._view.ClearMessageLabel()
            self._view.SetMessageLabel("Book successfully returned", 'green')
        except NonExistentBook as e:
            self._view.SetMessageLabel(e.message, 'red')
        except NumericValueOutOfRange:
            self._view.SetMessageLabel("Too big id copy value", 'red')
        except BaseFormatError as e:
             self._view.SetMessageLabel(e.message, 'red')
        except Exception as e:
            print(e)
            self._view.SetMessageLabel("Unexpected error", 'red')