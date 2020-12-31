import sys
import os
sys.path.append(os.path.abspath('Database'))
sys.path.append(os.path.abspath('Errors'))
from database import DatabaseManager
from Models.AbstractModel import AbstractModel

class BookSearchModel(AbstractModel):
    def __init__(self):
        self._observers = set()
