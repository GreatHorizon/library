

class StudentIssuancePageController:
    def __init__(self, window, model, view):
        self._window = window
        self._model = model
        self._view = view

    def BackToStudentPage(self):
        from Views.StudentPage import StudentPage
        self._window.show_frame(StudentPage)

    def GetStudentIssuance(self, id):
        return self._model.GetStudentIssuance(id)
