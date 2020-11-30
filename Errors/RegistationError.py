

class EmptyFieldError(Exception):
    def __init__(self, disc):
        self.message = disc
        super().__init__(self.message)


class UniqueEmailViolation(Exception):
    def __init__(self, disc):
        self.message = disc
        super().__init__(self.message)

class UniquePhoneViolation(Exception):
    def __init__(self, disc):
        self.message = disc
        super().__init__(self.message)

class UniqueIdViolation(Exception):
    def __init__(self, disc):
        self.message = disc
        super().__init__(self.message)       