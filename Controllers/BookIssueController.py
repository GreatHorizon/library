class BookIssueController:
    def __init__(self, window, model, view):
        self._view = view
        self._window = window
        self._model = model

    def GetStudentsId(self):
        studentsList = self._model.GetStudentsList()
        return studentsList
    
    def GetAuthors(self):
        booksList = self._model.GetAuthorList()
        return booksList

    def GetAuthorsBookByName(self, name):
        booksList = self._model.GetBooksByAuthorName

    def BackToAdminPage(self):
        from Views.AdminPage import AdminPage
        self._window.show_frame(AdminPage)