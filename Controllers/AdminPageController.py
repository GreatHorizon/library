
from Views.RegisterStudentPage import RegisterStudentPage
from Views.AdminAuthorizationPage import AdminAuthorizationPage
from Views.AddBookPage import AddBookPage
from Views.BookIssuePage import BookIssuePage 

class AdminPageController:
    def __init__(self, window, model, view):
        self._view = view
        self._window = window
        self._model = model

    def OpenStudentRegistrationPage(self):
        self._window.show_frame(RegisterStudentPage)

    def OpenAddBookPage(self):
        self._window.show_frame(AddBookPage)

    def BackToAdminAuthorizationPage(self):
        self._window.show_frame(AdminAuthorizationPage)

    def OpenBookIssuePage(self):
        self._window.show_frame(BookIssuePage)