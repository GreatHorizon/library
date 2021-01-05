
from Models.AdminPageModel import AdminPageModel

class StudentDebtsController:
    def __init__(self, master, model, view):
        self._master = master
        self._model = model
        self._view = view


    def BackToAdminPage(self):
        from Views.AdminPage import AdminPage
        self._master.switch_frame(AdminPage, AdminPageModel)

    def GetStudentsInfo(self, text):
        studentsList = self._model.GetStudentsList(text)
        return studentsList

    def GetStudentDebtsAndShowTable(self, text):
        if (not text):
            self._view.ClearTable()
        else:
            self._view.ClearTable()
            studentDebts = self._model.GetStudentDebts(text)
            self._view.FillTable(studentDebts)