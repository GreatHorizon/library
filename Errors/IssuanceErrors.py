class BaseIssuanceError(Exception):
    def __init__(self, disc):
        self.message = disc
        super().__init__(self.message)

class NonExistentStudent(BaseIssuanceError):
    pass

class NonExistentAuthor(BaseIssuanceError):
    pass
