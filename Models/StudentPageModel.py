

class StudentPageModel:
    def __init__(self):
        self._observers = set()
        self._isAuthorizated = False
        self._message = ''