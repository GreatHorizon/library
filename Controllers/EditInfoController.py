from Models.EditInfoModel import EditInfoModel
from Models.StudentPageModel import StudentPageModel

class EditInfoController:
    def __init__(self, master, model, view):
        self._master = master
        self._model = model
        self._view = view

    def BackToStudentPage(self):
        from Views.StudentPage import StudentPage
        self._master.switch_frame(StudentPage, StudentPageModel, self._model._studentId)
