from Models.StudentPageModel import StudentPageModel

class StudentIssuancePageController:
    def __init__(self, master, model, view):
        self._master = master
        self._model = model
        self._view = view

    def BackToStudentPage(self):
        from Views.StudentPage import StudentPage
        self._master.switch_frame(StudentPage, StudentPageModel, self._model._studentId)

    def GetStudentIssuance(self):
        studentIssuance = self._model.GetStudentIssuance()
        if (len(studentIssuance) == 0):
            self._view.ShowNoDataLabelWithText("You don't have issues yet.")
        else:
            self._view.FillTable(studentIssuance)
