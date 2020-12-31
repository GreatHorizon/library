

class BaseUniqueViolation(Exception):
    def __init__(self, disc):
        self.message = disc
        super().__init__(self.message)  

class UniqueEmailViolation(BaseUniqueViolation):
    pass
class UniquePhoneViolation(BaseUniqueViolation):
    pass
class UniqueIdViolation(BaseUniqueViolation):
    pass     