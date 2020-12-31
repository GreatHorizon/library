
from Views.RegisterStudentPage import RegisterStudentPage
from Views.AdminAuthorizationPage import AdminAuthorizationPage
from Views.AddBookPage import AddBookPage
from Views.BookIssuePage import BookIssuePage 
from Models.AdminAutorizationModel import AdminAuthorizationModel
from Models.RegisterStudentModel import RegisterStudentModel
from Models.AddBookModel import AddBookModel
from Models.BookIssueModel import BookIssueModel

class AdminPageController:
    def __init__(self, master, model, view):
        self._view = view
        self._master = master
        self._model = model

    def OpenStudentRegistrationPage(self):
        self._master.switch_frame(RegisterStudentPage, RegisterStudentModel)

    def OpenAddBookPage(self):
        self._master.switch_frame(AddBookPage, AddBookModel)

    def BackToAdminAuthorizationPage(self):
        self._master.switch_frame(AdminAuthorizationPage, AdminAuthorizationModel)

    def OpenBookIssuePage(self):
        self._master.switch_frame(BookIssuePage, BookIssueModel)

    
