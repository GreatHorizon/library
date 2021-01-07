import sys
import os
import psycopg2
from tkinter import messagebox
from dotenv import load_dotenv
project_folder = os.path.expanduser('../library')
load_dotenv(os.path.join(project_folder, '.env'))

sys.path.append(os.path.abspath('Utils'))
sys.path.append(os.path.abspath('Errors'))
sys.path.append(os.path.abspath('Config'))
from PasswordUtil import *
from AuthorizationErrors import *
from RegistationError import *
from Config import DEFAULT_PASSWORD
from DeleteBookErrors import *

from dotenv import load_dotenv
project_folder = os.path.expanduser('../library')
load_dotenv(os.path.join(project_folder, '.env'))

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
            # if author does not exists, we need to create him
            self.__cursor.execute("INSERT INTO author (name) VALUES (%s)", (str(author),))
            self.__cursor.execute('SELECT id_author FROM author WHERE name = %s', (str(author),))
        authorId = self.__cursor.fetchone()[0]

        # need to check, if author has book with this name but different isbn
        self.__cursor.execute('SELECT isbn FROM book ' +
            'INNER JOIN author_has_book on book.id_book = author_has_book.id_book ' +
            'INNER JOIN author on author.id_author = author_has_book.id_author ' + 
            'WHERE author.id_author = %s AND book.name = %s', (str(authorId), str(bookName)))

        if self.__cursor.rowcount != 0:
           if self.__cursor.fetchone()[0] != isbn:
               raise AddBookError("Author cant have books with same names and different isbn")

        self.__cursor.execute('SELECT name, id_book FROM book WHERE isbn = %s', (str(isbn),))
        if self.__cursor.rowcount == 0:
            #if book does not exists we need to create it
            self.__cursor.execute("INSERT INTO book (isbn, name) VALUES (%s, %s)", (str(isbn), str(bookName)))
            self.__cursor.execute('SELECT id_book FROM book WHERE isbn = %s', (str(isbn),))
            bookId = self.__cursor.fetchone()[0] 
            self.__cursor.execute("INSERT INTO author_has_book (id_book, id_author) VALUES (%s, %s)", (str(bookId), str(authorId)))
        else:
            # if book name already exists
            row = self.__cursor.fetchone()
            if  row[0] != bookName:
                #if book with different name and this isbn already exists - we cant create
                raise AddBookError("There is book with this isbn, but different name")
            bookId = row[1]  

        self.__cursor.execute("INSERT INTO copy (id_book,page_count, is_available, publisher)" + 
        "VALUES (%s, %s, 1, %s) RETURNING id_copy", (str(bookId), str(pageCount), str(publisher)))
        addedCopyId = self.__cursor.fetchone()[0]
        self.__connection.commit()
        return addedCopyId
        

    def InsertStudent(self, id, name, surname, birthday, phone, email):
        self.__cursor.execute('SELECT id_student FROM student WHERE id_student = %s', (id,))
        if (self.__cursor.rowcount != 0):
            raise UniqueIdViolation('Student id already used')
        self.__cursor.execute('SELECT email FROM student WHERE email = %s', (email,))
        if (self.__cursor.rowcount != 0):
            raise UniqueEmailViolation('Email already used')
        self.__cursor.execute('SELECT phone FROM student WHERE phone = %s', (phone,))
        if (self.__cursor.rowcount != 0):
            raise UniquePhoneViolation('Phone already used')
        self.__cursor.execute('INSERT INTO student VALUES (%s, %s, %s, to_date(%s, \'dd/mm/yyyy\'), %s, %s, decode(%s, \'hex\'))',
        (id, name, surname, birthday, email, phone, DEFAULT_PASSWORD))
        self.__connection.commit()
  
    def VerifyStudent(self, id , password):
        self.__cursor.execute('SELECT password FROM student WHERE id_student = ' + id)
        if self.__cursor.rowcount == 0:
            raise AuthorizationError("Incorrect login or password")
        actualPassword = bytes(self.__cursor.fetchone()[0])
        encodedPassword = GetEncodedPassword(password,  GetSaltPart(actualPassword))
        if (GetPasswordPart(actualPassword) != encodedPassword):
            raise AuthorizationError("Incorrect login or password")

    def UpdatePassword(self, id, newPassword):
        newEncodedPass = GenerateEncodedPassword(newPassword)
        self.__cursor.execute('UPDATE student SET password = decode(%s, \'hex\') WHERE id_student = %s', (newEncodedPass, id))
        self.__connection.commit()

    def CheckOldPassword(self, id, password):
        self.__cursor.execute('SELECT password FROM student WHERE id_student = ' + id)
        actualPassword = bytes(self.__cursor.fetchone()[0])
        encodedPassword = GetEncodedPassword(password,  GetSaltPart(actualPassword))
        if (GetPasswordPart(actualPassword) != encodedPassword):
            raise IncorrectPassword('Old password is wrong')
    
    def DeleteCopy(self, idCopy) :
        self.__cursor.execute('SELECT is_available FROM copy WHERE id_copy = %s', (idCopy,))
        copyStatus = self.__cursor.fetchone()
        if copyStatus is None:
            raise NonExistentBook("Book does not exitst")

        if copyStatus[0] == 0 :
            raise BookIsNotAvailable("Book now is in issue")

        self.__cursor.execute('DELETE FROM copy WHERE id_copy = %s RETURNING id_copy', (idCopy,))
        self.__connection.commit()

    def GetStudentsInfoPart(self, textPart):
        print(textPart)
        self.__cursor.execute("""
                    SELECT id_student FROM student
                    WHERE CAST(id_student AS VARCHAR) LIKE '%%{0}%%'
                    """.format(textPart))
        return self.__cursor.fetchall()
    
    def GetStudentIssuance(self, id):
        self.__cursor.execute('SELECT copy.id_copy, book.name, author.name, start, "end" FROM student ' +
            'INNER JOIN issue ON student.id_student = issue.id_student ' +
            'INNER JOIN copy ON copy.id_copy = issue.id_copy ' +
            'INNER JOIN book ON copy.id_book = book.id_book ' +
            'INNER JOIN author_has_book on author_has_book.id_book = book.id_book ' +
            'INNER JOIN  author ON author_has_book.id_author = author.id_author ' +
            'WHERE copy.is_available = 0 AND student.id_student = %s', (id,))
        return self.__cursor.fetchall()

    def GetAuthorList(self, text):
        print(text)
        self.__cursor.execute("""
                SELECT name FROM author WHERE name ILIKE '%%{0}%%'
        """.format(text))
        return self.__cursor.fetchall()
        
    def GetBooksList(self, text):
        self.__cursor.execute("""
                SELECT DISTINCT name FROM book WHERE name ILIKE '%%{0}%%'
        """.format(text))
        return self.__cursor.fetchall()

    def SearchBooksByName(self, name):
        self.__cursor.execute('SELECT distinct copy.id_book, temp.name, author.name, copyCount, copy.page_count, copy.publisher FROM ' +
        '(SELECT book.id_book, book.isbn, book.name, count(book.id_book) as copyCount FROM book ' +
        'INNER JOIN copy on book.id_book = copy.id_book ' +
        'INNER JOIN author_has_book on author_has_book.id_book = book.id_book ' +
        'INNER JOIN author on author.id_author = author_has_book.id_author ' +
        'WHERE book.name = %s and is_available = 1' +
        'GROUP BY book.id_book) AS temp ' +
        'INNER JOIN copy on copy.id_book = temp.id_book '
        'INNER JOIN author_has_book on copy.id_book = author_has_book.id_book '
        'INNER JOIN author on author.id_author = author_has_book.id_author ', (str(name),))
        return self.__cursor.fetchall()
    
    def SearchBooksByAuthor(self, name):
        self.__cursor.execute('SELECT distinct copy.id_book, temp.name, author.name, copyCount, copy.page_count, copy.publisher FROM ' +
            '(SELECT book.id_book, book.isbn, book.name, count(book.id_book) as copyCount FROM author ' +
            'INNER JOIN author_has_book on author.id_author = author_has_book.id_author ' +
            'INNER JOIN book on book.id_book = author_has_book.id_book ' +
            'INNER JOIN copy on book.id_book = copy.id_book ' +
            'WHERE author.name = %s and is_available = 1 ' +
            'GROUP BY book.id_book ' +
            ') AS temp ' +
            'INNER JOIN copy on copy.id_book = temp.id_book ' + 
            'INNER JOIN author_has_book on copy.id_book = author_has_book.id_book ' +
            'INNER JOIN author on author.id_author = author_has_book.id_author', (str(name),))
        return self.__cursor.fetchall()

    def GetAuthorBooks(self, name):
        self.__cursor.execute("""
                SELECT book_name FROM author
                INNER JOIN author_has_book ON author.id_author = author_has_book.id_author
                INNER JOIN
                (SELECT id_book,name AS book_name FROM book) AS book
                ON book.id_book = author_has_book.id_book
                WHERE name = %s
            """, 
            (name,))
        return self.__cursor.fetchall()

    def GetCopies(self, name):
        self.__cursor.execute("""
                SELECT id_copy FROM copy
                INNER JOIN (SELECT id_book, isbn, name FROM book) AS book ON book.id_book = copy.id_book
                WHERE name = %s AND is_available = 1
        """,
        (name,))
        return self.__cursor.fetchall()

    def GetStudentById(self, id):
        self.__cursor.execute("""
                SELECT id_student FROM student WHERE id_student = %s
        """,
        (id,))
        return self.__cursor.fetchone()

    def GetAuthorByName(self, name):
        self.__cursor.execute("""
                SELECT name FROM author WHERE name = %s
        """,
        (name,))
        return self.__cursor.fetchone()

    def InsertIssuance(self, studentId, copy, start, end):
        self.__cursor.execute("""
                INSERT INTO issue VALUES(DEFAULT, %s, %s, %s, %s)
        """,
        (studentId, copy, start, end,))

    def UpdateCopyStateToUnavailable(self, copy):
        self.__cursor.execute("""
                UPDATE copy SET is_available = 0 WHERE id_copy = %s
        """,
        (copy,))

    def UpdateCopyStateToAvailable(self, idCopy):
        self.__cursor.execute("""
                UPDATE copy SET is_available = 1 WHERE id_copy = %s RETURNING id_copy
        """,
        (idCopy,))
        return self.__cursor.fetchone()

    def GetCopyState(self, idCopy):
        self.__cursor.execute("""
           SELECT is_available FROM copy WHERE id_copy = %s
        """,
        (idCopy,))
        return self.__cursor.fetchone()
        

    def DeleteStudentIssue(self, idCopy):
        self.__cursor.execute("""
                DELETE FROM issue WHERE id_copy = %s
        """,
        (idCopy,))

    def GetStudentIdByIssuedCopyId(self, idCopy):
        self.__cursor.execute("""
                SELECT id_student FROM issue
                WHERE id_copy = %s
        """, (idCopy,))
        return self.__cursor.fetchone()

    def CommitChanges(self):
        self.__connection.commit()


    def __del__(self):
        self.__cursor.close()
        self.__connection.commit()
        self.__connection.close()