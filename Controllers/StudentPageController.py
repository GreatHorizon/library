
from Views.StudentAuthorizationPage import StudentAuthorizationPage

class StudentPageController:
    def __init__(self, window, model, view):
        self._window = window
        self._model = model
        self._view = view

    def BackToStudentAuthorizationPage(self):
        self._window.show_frame(StudentAuthorizationPage)