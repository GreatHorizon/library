

class AddBookController:
    def __init__(self, window, model, view):
        self._window = window
        self._model = model
        self._view = view

    def BackToAdminPage(self):
        from Views.AdminPage import AdminPage
        self._window.show_frame(AdminPage)
        self._view.ClearFields()

    def AddBook(self, isbn, bookName, author, pageCount, publisher):
        self._model.AddBook(isbn, bookName, author, pageCount, publisher)