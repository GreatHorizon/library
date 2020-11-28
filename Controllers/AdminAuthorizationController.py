
class AdminAuthorizationController:
    def __init__(self, window, model, view):
        self._window = window
        self._model = model
        self._view = view

    def BackToStartPage(self):
        from Views.StartPage import StartPage
        self._window.show_frame(StartPage)
        self._view.ClearFields()
        self._view.ClearErrorLabel()

    def SignInAdmin(self, adminId, password):
        self._model.VerifyAdmin(adminId, password)

    def OpenAdminPage(self):
        from Views.AdminPage import AdminPage
        self._window.show_frame(AdminPage)