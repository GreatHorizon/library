
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


    def ReturnBooks(self, idCopies):
        if (len(idCopies) > 0):
            try:
                id = self._model.GetStudentId(idCopies[0])
                self._model.ReturnBooks(idCopies)
                self._view.ClearTable()
                studentDebts = self._model.GetStudentDebts(id)
                self._view.FillTable(studentDebts)
                singOrPlural = 'Book'
                if (len(idCopies) > 1):
                    singOrPlural = 'Books'
                self._view.SetMessageLabel(singOrPlural + " successfully returned" , "green")
            except Exception as e:
                print(e)
                self._view.SetMessageLabel("Something went wrong", "red")
        else:
            self._view.SetMessageLabel("0 books have been selected. Nothing to return", "red")

        