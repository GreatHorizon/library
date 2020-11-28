
from Views.RegisterStudentPage import RegisterStudentPage
from Views.AdminAuthorizationPage import AdminAuthorizationPage

class AdminPageController:
    def __init__(self, window, model, view):
        self._view = view
        self._window = window
        self._model = model

    def OpenStudentRegistrationPage(self):
        self._window.show_frame(RegisterStudentPage)

    def BackToAdminAuthorizationPage(self):
        self._window.show_frame(AdminAuthorizationPage)