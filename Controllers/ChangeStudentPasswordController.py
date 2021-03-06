
from Models.StudentPageModel import StudentPageModel

class ChangeStudentPasswordController:
    def __init__(self, master, model, view):
        self._view = view
        self._master = master
        self._model = model

    def BackToStudentPage(self):
        from Views.StudentPage import StudentPage
        self._master.switch_frame(StudentPage, StudentPageModel, self._model._studentId)

    def ChangePassword(self, old, new, conf):
        self._model.SetNewPassword(old, new, conf)