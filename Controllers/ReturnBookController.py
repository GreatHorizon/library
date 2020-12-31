from Models.ReturnBookModel import ReturnBookModel

class ReturnBookController:
    def __init__(self, master, model, view):
        self._view = view
        self._master = master
        self._model = model
