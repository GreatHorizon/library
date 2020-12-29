
from Views.StudentAuthorizationPage import StudentAuthorizationPage
from Views.ChangeStudentPasswordPage import ChangeStudentPasswordPage
from Views.StudentIssuancePage import StudentIssuancePage

class StudentPageController:
    def __init__(self, window, model, view):
        self._window = window
        self._model = model
        self._view = view

    def BackToStudentAuthorizationPage(self):
        self._window.show_frame(StudentAuthorizationPage)

    def OpenChangePasswordPage(self):
        self._window.show_frame(ChangeStudentPasswordPage)
        self._window.send_data(ChangeStudentPasswordPage, id=self._model._studentId)

    def OpenStudentIssuanceList(self) :
        self._window.show_frame(StudentIssuancePage)
        # StudentIssuancePage.updateView(self)
        self._window.send_data(StudentIssuancePage, id=self._model._studentId)

    def SaveData(self, id):
        self._model.SaveStudentId(id)

    def GetStudentIssuance(self, id):
        return self._model.GetStudentIssuance(id)

    