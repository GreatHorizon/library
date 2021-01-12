
from Views.AdminAuthorizationPage import AdminAuthorizationPage
from Views.StudentAuthorizationPage import StudentAuthorizationPage
from Views.BookSearchPage import BookSearchPage
from Models.AdminAutorizationModel import AdminAuthorizationModel
from Models.StudentAuthorizationModel import StudentAuthorizationModel
from Models.BookSearchModel import BookSearchModel


class StartPageController:
    def __init__(self, master, model, view):
        self._view = view
        self._model = model
        self._master = master

    def openAdminAuthorizationPage(self):
        self._master.switch_frame(AdminAuthorizationPage, AdminAuthorizationModel)
    
    def openStudentAuthorizationPage(self):
        self._master.switch_frame(StudentAuthorizationPage, StudentAuthorizationModel)

    def OpenBookSearchPage(self):
        self._master.switch_frame(BookSearchPage, BookSearchModel)