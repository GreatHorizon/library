

class DeleteCopyController:
    def __init__(self, window, model, view):
        self._window = window
        self._model = model
        self._view = view
    
    def BackToAdminPage(self):
        from Views.AdminPage import AdminPage
        self._window.show_frame(AdminPage)

    def DeleteCopy(self, copyId):
        self._model.DeleteCopy(copyId)
