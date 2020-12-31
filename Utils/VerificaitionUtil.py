import sys
import os
sys.path.append(os.path.abspath('Errors'))
from FormatErrors import *

def IsEmpty(str):
    return not str


def IsNumber(id):
    if not str.isdigit(id) or id == "":
        raise InvalidFormatForDigit('Not number')
