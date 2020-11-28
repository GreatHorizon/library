import sys
import os
import psycopg2
from tkinter import messagebox

sys.path.append(os.path.abspath('Utils'))
sys.path.append(os.path.abspath('Errors'))

from PasswordUtil import *
from AuthorizationErrors import *


class DatabaseManager:
    def __init__(self):
        conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost')
        cursor = conn.cursor()
        self.__connection = conn
        self.__cursor = cursor

    def FindUser(self, studentId):
        self.__cursor.execute('SELECT * FROM student WHERE id_student = ' + studentId)
        if self.__cursor.rowcount == 0:
            raise ValueError("Incorrect id specified")

    def VerifyAdmin(self, adminId, password):
        self.__cursor.execute('SELECT * FROM admin WHERE id_admin = ' + adminId)
        if self.__cursor.rowcount == 0:
            raise AuthorizationError("Incorrect login or password")
        actualPassword = bytes(self.__cursor.fetchone()[0])
        encodedPassword = GetEncodedPassword(password,  GetSaltPart(actualPassword))
        if (GetPasswordPart(actualPassword) != encodedPassword):
            raise AuthorizationError("Incorrect login or password")

  
    def __del__(self):
        self.__cursor.close()
        self.__connection.close()