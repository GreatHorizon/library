
from Views.RegisterStudentPage import RegisterStudentPage
from Views.AdminAuthorizationPage import AdminAuthorizationPage
from Views.AddBookPage import AddBookPage
from Views.BookIssuePage import BookIssuePage 
from Views.ReturnBookPage import ReturnBookPage
from Models.AdminAutorizationModel import AdminAuthorizationModel
from Models.RegisterStudentModel import RegisterStudentModel
from Models.AddBookModel import AddBookModel
from Models.BookIssueModel import BookIssueModel
from Models.ReturnBookModel import ReturnBookModel

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

    def OpenReturnBookPage(self):
        self._master.switch_frame(ReturnBookPage, ReturnBookModel)

    
    def OpenDeleteBookPage(self):
        self._master.switch_frame(DeleteCopyPage, DeleteCopyModel)
