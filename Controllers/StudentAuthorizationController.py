from Models.StartPageModel import StartPageModel
from Models.StudentPageModel import StudentPageModel

class StudentAuthorizationController:
    def __init__(self, master, model, view):
        self._master = master
        self._model = model
        self._view = view

    def BackToStartPage(self):
        from Views.StartPage import StartPage
        self._master.switch_frame(StartPage, StartPageModel)

    def SignInStudent(self, id , password):
        self._model.VerifyStudent(id, password)

    def OpenStudentPage(self):
        from Views.StudentPage import StudentPage
        self._master.switch_frame(StudentPage, StudentPageModel, self._model._userId)

    def SendData(self, **data):
        from Views.StudentPage import StudentPage
        self._master.send_data(StudentPage, **data)
