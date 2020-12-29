
class EmptyFieldError(Exception):
    def __init__(self, disc):
        self.message = disc
        super().__init__(self.message)