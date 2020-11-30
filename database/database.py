import sys
import os
import psycopg2
from tkinter import messagebox
from dotenv import load_dotenv
project_folder = os.path.expanduser('../library')
load_dotenv(os.path.join(project_folder, '.env'))

sys.path.append(os.path.abspath('Utils'))
sys.path.append(os.path.abspath('Errors'))

from PasswordUtil import *
from AuthorizationErrors import *


class DatabaseManager:
    def __init__(self):
        conn = psycopg2.connect(dbname=os.getenv("DB_NAME"), user=os.getenv("USER"), password=os.getenv("PASSWORD"), host=os.getenv("HOST"))
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
        actualPassword = bytes(self.__cursor.fetchone()[1])
        encodedPassword = GetEncodedPassword(password,  GetSaltPart(actualPassword))
        if (GetPasswordPart(actualPassword) != encodedPassword):
            raise AuthorizationError("Incorrect login or password")

    def InsertBook(self, isbn, bookName, author, pageCount, publisher) :
        self.__cursor.execute('SELECT id_author FROM author WHERE name = %s', (str(author),))
        if self.__cursor.rowcount == 0:
            self.__cursor.execute("INSERT INTO author (name) VALUES (%s)", (str(author),))
            self.__cursor.execute('SELECT id_author FROM author WHERE name = %s', (str(author),))
        authorId = self.__cursor.fetchone()[0]

        self.__cursor.execute('SELECT name, id_book FROM book WHERE isbn = %s', (str(isbn),))
        if self.__cursor.rowcount == 0:
            self.__cursor.execute("INSERT INTO book (isbn, name) VALUES (%s, %s)", (str(isbn), str(bookName)))
            self.__cursor.execute('SELECT id_book FROM book WHERE isbn = %s', (str(isbn),))
            bookId = self.__cursor.fetchone()[0] 
            self.__cursor.execute("INSERT INTO author_has_book (id_book, id_author) VALUES (%s, %s)", (str(bookId), str(authorId)))
        else:
            row = self.__cursor.fetchone()
            if  row[0] != bookName:
                raise AddBookError("There is book with this isbn, but different name")
            bookId = row[1]  

        self.__cursor.execute("INSERT INTO copy (id_book, page_count, publisher) VALUES (%s, %s, %s)", (str(bookId), str(pageCount), str(publisher)))
        self.__connection.commit()

    def __del__(self):
        self.__cursor.close()
        self.__connection.close()