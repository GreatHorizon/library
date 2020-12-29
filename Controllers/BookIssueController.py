from  Models.AdminPageModel import AdminPageModel

class BookIssueController:
    def __init__(self, master, model, view):
        self._view = view
        self._master = master
        self._model = model

    def GetStudentsId(self):
        studentsList = self._model.GetStudentsList()
        print(studentsList)
        return studentsList
    
    def GetAuthors(self):
        booksList = self._model.GetAuthorList()
        return booksList

    # def GetAuthorsBookByName(self, name):
    #     booksList = self._model.GetAuthorBooksByName(name)
    #     print(booksList)

    def BackToAdminPage(self):
        from Views.AdminPage import AdminPage
        self._master.switch_frame(AdminPage, AdminPageModel)

    def EnableBooksList(self, authorName):
        if (not authorName):
            self._view.DisableBooksList()
        booksList = self._model.GetAuthorBooksByName(authorName)
        self._view.EnableBooksListAndFillValues(booksList)

    def EnableCopiesList(self, event):
        copies = self._model.GetBookCopies(event.widget.get())
        self._view.EnableCopiesListAndFillValues(copies)

    def CreateIssue(self, studentId, author, book, copy, start, end):
        self._model.CreateIssue(studentId, author, book, copy, start, end)