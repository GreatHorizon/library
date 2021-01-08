
from Views.StudentAuthorizationPage import StudentAuthorizationPage
from Views.ChangeStudentPasswordPage import ChangeStudentPasswordPage
from Views.StudentIssuancePage import StudentIssuancePage
from Views.BookSearchPage import BookSearchPage
from Views.EditInfoPage import EditInfoPage
from Models.StudentAuthorizationModel import StudentAuthorizationModel
from Models.StudentIssuanceModel import StudentIssuanceModel
from Models.ChangeStudentPasswordModel import ChangeStudentPasswordModel
from Models.BookSearchModel import BookSearchModel
from Models.EditInfoModel import EditInfoModel



class StudentPageController:
    def __init__(self, master, model, view):
        self._master = master
        self._model = model
        self._view = view

    def BackToStudentAuthorizationPage(self):
        self._master.switch_frame(StudentAuthorizationPage, StudentAuthorizationModel)

    def OpenChangePasswordPage(self):
        self._master.switch_frame(ChangeStudentPasswordPage, ChangeStudentPasswordModel, self._model._studentId)

    def OpenEditInfoPage(self):
        self._master.switch_frame(EditInfoPage, EditInfoModel, self._model._studentId)

    def OpenStudentIssuanceList(self):
        self._master.switch_frame(StudentIssuancePage, StudentIssuanceModel, self._model._studentId)

    def OpenBookSearchPage(self):
        self._master.switch_frame(BookSearchPage, BookSearchModel, self._model._studentId)

    def GetStudentInfo(self):
        return self._model.GetStudentInfo()





    