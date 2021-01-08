

from Models.AdminPageModel import AdminPageModel

class EditBookController():
    def __init__(self, master, model, view):
        self._master = master
        self._model = model
        self._view = view


    def BackToAdminPage(self):
        from Views.AdminPage import AdminPage
        self._master.switch_frame(AdminPage, AdminPageModel)
    