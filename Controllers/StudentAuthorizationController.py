class StudentAuthorizationController:
    def __init__(self, window, model, view):
        self._window = window
        self._model = model
        self._view = view

    def BackToStartPage(self):
        from Views.StartPage import StartPage
        self._window.show_frame(StartPage)
        self._view.ClearFields()
        self._view.ClearErrorLabel()

    def SignInStudent(self, id , password):
        self._model.VerifyStudent(id, password)

    def OpenStudentPage(self):
        from Views.StudentPage import StudentPage
        self._window.show_frame(StudentPage)

    def SendData(self, **data):
        from Views.StudentPage import StudentPage
        self._window.send_data(StudentPage, **data)