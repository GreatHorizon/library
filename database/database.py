import psycopg2
from tkinter import messagebox

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

    def __del__(self):
        self.__cursor.close()
        self.__connection.close()