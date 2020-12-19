
class ChangeStudentPasswordController:
    def __init__(self, window, model, view):
        self._view = view
        self._window = window
        self._model = model

    def BackToStudentPage(self):
        from Views.StudentPage import StudentPage
        self._window.show_frame(StudentPage)
        self._view.ClearFields()
        self._view.ClearMessageLabel()

    def ChangePassword(self, id, old, new, conf):
        self._model.SetNewPassword(id, old, new, conf)