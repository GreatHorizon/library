import psycopg2
from tkinter import messagebox

from .. import PasswordUtil

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
            raise ValueError("Incorrect id specified")
        actualPassword = [row[1] for row in self.__cursor]
        encodedPassword = GetEncodedPassword(password, actualPassword[:32])
        if (actualPassword != encodedPassword):
            raise ValueError("Incorrect password specified")

  
    def __del__(self):
        self.__cursor.close()
        self.__connection.close()