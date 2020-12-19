class BookIssueController:
    def __init__(self, window, model, view):
        self._view = view
        self._window = window
        self._model = model

    def OpenIssueBookPage(self):
        from Views.BookIssuePage import BookIssuePage 
        self._window.show_frame(BookIssuePage)