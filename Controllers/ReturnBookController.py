from Models.ReturnBookModel import ReturnBookModel
from Models.AdminPageModel import AdminPageModel

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
        except:
            pass