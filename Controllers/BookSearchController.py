from  Models.StudentPageModel import StudentPageModel

class BookSearchController:
    def __init__(self, master, model, view):
        self._view = view
        self._master = master
        self._model = model    
        
    def BackToStudentPage(self):
        from Views.StudentPage import StudentPage
        self._master.switch_frame(StudentPage, StudentPageModel)

    def SetSearchStrategy(self, event):
        self._view.searchSelect.set_value('')
        self._view.ClearTable()
        if event.widget.get() == "Book name":
            self._model._searchStrategy = self._model.SearchByBookNameStrategy
            self._model._showStrategy = self._model.ShowByBookNameStrategy
        if event.widget.get() == "Author":
            self._model._searchStrategy = self._model.SearchByAuthorStrategy
            self._model._showStrategy = self._model.ShowByAuthorNameStrategy
            

    def GetSelectValues(self, text):
        return self._model._searchStrategy(text)

    def SearchBooks(self, text):
        if (not text):
            self._view.ClearTable()
        else:
            self._view.ClearTable()
            books = self._model._showStrategy(text)
            self._view.FillTable(books)