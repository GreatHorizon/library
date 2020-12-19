

class BookIssueModel:
    def __init__(self):
        self._observers = set()
        self._isChanged= False
        self._message = ''