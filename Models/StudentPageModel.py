
from Models.AbstractModel import AbstractModel

class StudentPageModel(AbstractModel):
    def __init__(self):
        self._studentId = int()

    def Save(self, data):
        self._studentId = data[0]