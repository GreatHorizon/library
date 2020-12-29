
from Views.StudentAuthorizationPage import StudentAuthorizationPage
from Views.ChangeStudentPasswordPage import ChangeStudentPasswordPage
from Views.StudentIssuancePage import StudentIssuancePage
from Models.StudentAuthorizationModel import StudentAuthorizationModel
from Models.StudentIssuanceModel import StudentIssuanceModel
from Models.ChangeStudentPasswordModel import ChangeStudentPasswordModel

class StudentPageController:
    def __init__(self, master, model, view):
        self._master = master
        self._model = model
        self._view = view

    def BackToStudentAuthorizationPage(self):
        self._master.switch_frame(StudentAuthorizationPage, StudentAuthorizationModel)

    def OpenChangePasswordPage(self):
        self._master.switch_frame(ChangeStudentPasswordPage, ChangeStudentPasswordModel, self._model._studentId)

    def OpenStudentIssuanceList(self):
        self._master.switch_frame(StudentIssuancePage, StudentIssuanceModel)
        # StudentIssuancePage.updateView(self)

    def GetStudentIssuance(self, id):
        return self._model.GetStudentIssuance(id)

    