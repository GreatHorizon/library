from Models.AdminPageModel import AdminPageModel

class RegisterStudentController:
    def __init__(self, window, model, view):
        self._window = window
        self._model = model
        self._view = view
    
    def BackToAdminPage(self):
        from Views.AdminPage import AdminPage
        self._window.switch_frame(AdminPage, AdminPageModel)

    def RegisterStudent(self, id, name, surname, birthday, phone, email):
        self._model.RegisterNewStudent(id, name, surname, birthday, phone, email)
