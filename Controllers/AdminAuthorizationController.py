from Models.StartPageModel import StartPageModel
from Models.AdminPageModel import AdminPageModel

class AdminAuthorizationController:
    def __init__(self, master, model, view):
        self._master = master
        self._model = model
        self._view = view

    def BackToStartPage(self):
        from Views.StartPage import StartPage
        self._master.switch_frame(StartPage, StartPageModel)

    def SignInAdmin(self, adminId, password):
        self._model.VerifyAdmin(adminId, password)

    def OpenAdminPage(self):
        from Views.AdminPage import AdminPage
        self._master.switch_frame(AdminPage , AdminPageModel)
