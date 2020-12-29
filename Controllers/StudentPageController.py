
from Views.StudentAuthorizationPage import StudentAuthorizationPage
from Views.ChangeStudentPasswordPage import ChangeStudentPasswordPage
from Views.StudentIssuancePage import StudentIssuancePage
from Models.StudentAuthorizationModel import StudentAuthorizationModel
from Models.StudentIssuanceModel import StudentIssuanceModel

class StudentPageController:
    def __init__(self, master, model, view):
        self._master = master
        self._model = model
        self._view = view

    def BackToStudentAuthorizationPage(self):
        self._master.switch_frame(StudentAuthorizationPage, StudentAuthorizationModel)

    def OpenChangePasswordPage(self):
        self._master.show_frame(ChangeStudentPasswordPage)
        self._master.send_data(ChangeStudentPasswordPage, id=self._model._studentId)

    def OpenStudentIssuanceList(self):
        self._master.switch_frame(StudentIssuancePage, StudentIssuanceModel)
        # StudentIssuancePage.updateView(self)
        self._master.send_data(self._model._studentId)

    def GetStudentIssuance(self, id):
        return self._model.GetStudentIssuance(id)

    