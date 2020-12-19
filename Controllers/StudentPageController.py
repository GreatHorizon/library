
from Views.StudentAuthorizationPage import StudentAuthorizationPage
from Views.ChangeStudentPasswordPage import ChangeStudentPasswordPage

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

    def SaveData(self, id):
        self._model.SaveStudentId(id)

    