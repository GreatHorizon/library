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

    def AddBook(self, isbn, bookName, author, pageCount, publisher) :
        existedAuthor = self.GetBookAuthor(isbn)
        if existedAuthor != None and existedAuthor[0] != author:
            raise AddBookError('This isbn already belongs to other author')

        authorId = self.GetAuthorId(author)
        if authorId == None:
            authorId = self.CreateAuthor(author)

        existedBook = self.GetAuthorsBook(authorId[0], bookName)
        if existedBook != None:
           if existedBook[0] != isbn:
               raise AddBookError("Author cant have books with same names and different isbn")

        book = self.GetBook(isbn)
        if book == None:
            bookId = self.CreateBook(isbn, bookName, authorId[0])
        else:
            if book[0] != bookName:
                raise AddBookError("There is book with this isbn, but different name")
            bookId = book[1]  

        addedCopyId = self.InsertCopy(bookId, pageCount, publisher)
        self.__connection.commit()
        return addedCopyId
    
    def CreateAuthor(self, author):
        self.__cursor.execute("INSERT INTO author (name) VALUES (%s) RETURNING id_author", (str(author),))
        return self.__cursor.fetchone()

    def GetAuthorId(self, author) :
        self.__cursor.execute('SELECT id_author FROM author WHERE name = %s', (str(author),))
        return self.__cursor.fetchone()

    def GetBook(self, isbn) :
        self.__cursor.execute('SELECT name, id_book FROM book WHERE isbn = %s', (str(isbn),))
        return self.__cursor.fetchone()

    def CreateBook(self, isbn, bookName, authorId):
        self.__cursor.execute("INSERT INTO book (isbn, name) VALUES (%s, %s) RETURNING id_book", (str(isbn), str(bookName)))
        bookId = self.__cursor.fetchone()[0] 
        self.__cursor.execute("INSERT INTO author_has_book (id_book, id_author) VALUES (%s, %s)", (str(bookId), str(authorId)))
        return bookId

    def GetAuthorsBook(self, authorId, bookName):
        self.__cursor.execute('SELECT isbn FROM book ' +
            'INNER JOIN author_has_book on book.id_book = author_has_book.id_book ' +
            'INNER JOIN author on author.id_author = author_has_book.id_author ' + 
            'WHERE author.id_author = %s AND book.name = %s', (str(authorId), str(bookName)))
        return self.__cursor.fetchone()

    def GetBookAuthor(self, isbn) :
        self.__cursor.execute('SELECT author.name FROM author ' + 
            'INNER JOIN author_has_book on author.id_author = author_has_book.id_author ' +
            'INNER JOIN book on book.id_book = author_has_book.id_book ' +
            'WHERE isbn = %s', (str(isbn),))
        return self.__cursor.fetchone()

    def InsertCopy(self, bookId, pageСount, publisher) :
        self.__cursor.execute("INSERT INTO copy (id_book, page_count, is_available, publisher)" + 
        "VALUES (%s, %s, 1, %s) RETURNING id_copy", (str(bookId), str(pageСount), str(publisher)))
        return self.__cursor.fetchone()[0]

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
        self.__cursor.execute("""
                    SELECT id_student FROM student
                    WHERE CAST(id_student AS VARCHAR) LIKE '%%{0}%%'
                    """.format(textPart))
        return self.__cursor.fetchall()
    
    def GetStudentIssuance(self, id):
        self.__cursor.execute('SELECT author.name, book.name, copy.id_copy, start, "end" FROM student ' +
            'INNER JOIN issue ON student.id_student = issue.id_student ' +
            'INNER JOIN copy ON copy.id_copy = issue.id_copy ' +
            'INNER JOIN book ON copy.id_book = book.id_book ' +
            'INNER JOIN author_has_book on author_has_book.id_book = book.id_book ' +
            'INNER JOIN  author ON author_has_book.id_author = author.id_author ' +
            'WHERE copy.is_available = 0 AND student.id_student = %s', (id,))
        return self.__cursor.fetchall()

    def GetAuthorList(self, text):
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
        self.__cursor.execute('SELECT temp.id_book, temp.name, author.name, copyCount, temp.page_count, temp.publisher FROM' +
        '(SELECT book.id_book, book.isbn, book.name, count(book.id_book) as copyCount, page_count, publisher FROM book ' +
        'INNER JOIN copy on book.id_book = copy.id_book ' +
        'INNER JOIN author_has_book on author_has_book.id_book = book.id_book ' +
        'INNER JOIN author on author.id_author = author_has_book.id_author ' +
        'WHERE book.name = %s and is_available = 1' +
        'GROUP BY book.id_book, publisher, page_count) AS temp ' +
        'INNER JOIN author_has_book on temp.id_book = author_has_book.id_book '
        'INNER JOIN author on author.id_author = author_has_book.id_author ', (str(name),))
        return self.__cursor.fetchall()
    
    def SearchBooksByAuthor(self, name):
        self.__cursor.execute('SELECT temp.id_book, temp.name, author.name, copyCount, temp.page_count, temp.publisher FROM ' +
            '(SELECT book.id_book, book.isbn, book.name, count(book.id_book) as copyCount, page_count, publisher FROM author ' +
            'INNER JOIN author_has_book on author.id_author = author_has_book.id_author ' +
            'INNER JOIN book on book.id_book = author_has_book.id_book ' +
            'INNER JOIN copy on book.id_book = copy.id_book ' +
            'WHERE author.name = %s and is_available = 1 ' +
            'GROUP BY book.id_book, publisher, page_count ' +
            ') AS temp ' +
            'INNER JOIN author_has_book on temp.id_book = author_has_book.id_book ' +
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

    def GetStudentInfo(self, studentId):
        self.__cursor.execute("SELECT first_name, last_name, birthday, email, phone FROM student WHERE id_student = %s", (studentId,))
        return self.__cursor.fetchone()

    def UpdatePhone(self, studentId, newPhone):
        self.__cursor.execute("SELECT id_student FROM student WHERE phone = %s", (str(newPhone),))

        if self.__cursor.rowcount != 0 and int(self.__cursor.fetchone()[0]) != int(studentId):
            raise UniquePhoneViolation("Phone is busy")
        
        self.__cursor.execute("UPDATE student SET phone = %s WHERE student.id_student = %s", (newPhone, studentId))
        self.__connection.commit()

    def UpdateEmail(self, studentId, newEmail):
        self.__cursor.execute("SELECT id_student FROM student WHERE email = %s", (str(newEmail),))
        if self.__cursor.rowcount != 0 and int(self.__cursor.fetchone()[0]) != int(studentId):
            raise UniqueEmailViolation("Email is busy")

        self.__cursor.execute("UPDATE student SET email = %s WHERE student.id_student = %s", (newEmail, studentId))
        self.__connection.commit()

    def GetStudentById(self, id):
        self.__cursor.execute("""
                SELECT id_student FROM student WHERE id_student = %s
        """,
        (id,))
        return self.__cursor.fetchone()

    def GetAuthorByName(self, name):
        # can break something
        self.__cursor.execute("""
                SELECT id_author FROM author WHERE name = %s
        """,
        (name,))
        return self.__cursor.fetchone()

    def InsertIssuance(self, studentId, copy, start, end):
        self.__cursor.execute("""
                INSERT INTO issue VALUES(DEFAULT, %s, %s, %s, %s)
        """,
        (studentId, copy, start, end,))

    def GetStudentInfoById(self, id):
        self.__cursor.execute("""
                SELECT first_name, last_name, email, phone FROM student WHERE id_student = %s
        """,
        (id, ))
        return self.__cursor.fetchone()

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

    def GetCopyInfoById(self, id):
        self.__cursor.execute("""
                SELECT page_count, publisher FROM copy WHERE id_copy = %s
        """,
        (id,))
        return self.__cursor.fetchone()

    def UpdateCopyInfo(self, idCopy, newPagesCount, newPublisherName):
        self.__cursor.execute("""
                UPDATE copy SET page_count = %s, publisher = %s  WHERE id_copy = %s
        """,
        (newPagesCount, newPublisherName, idCopy))

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

    def UpdateAuthorBookName(self, idBook, newBookName):   
        self.__cursor.execute("""
                UPDATE book SET name = %s WHERE id_book = %s 
        """,
        (newBookName, idBook))

    def GetIdBookByNameAndAuthorId(self, bookName, idAuthor):
        self.__cursor.execute("""
                SELECT book.id_book FROM author
                INNER JOIN author_has_book ON author.id_author = author_has_book.id_author
				INNER JOIN book ON book.id_book = author_has_book.id_book
                WHERE author.id_author = %s AND book.name = %s
        """,
        (idAuthor, bookName))
        return self.__cursor.fetchone()

    def InsertNewAuthor(self, authorName):
        self.__cursor.execute("""
                INSERT INTO author (name) VALUES (%s) RETURNING id_author
        """, (authorName,))
        return self.__cursor.fetchone()

    def UpdateBookNameById(self, newName, idBook):
        self.__cursor.execute("""
                UPDATE book SET name = %s WHERE id_book = %s 
        """,
        (newName, idBook))

    def DeleteBookFromOldAuthor(self, oldAuthorId, idBook):
        self.__cursor.execute("""
                DELETE FROM author_has_book WHERE id_book = %s AND id_author = %s
        """,
        (idBook, oldAuthorId))

    def GetStudentIdByIssuedCopyId(self, idCopy):
        self.__cursor.execute("""
                SELECT id_student FROM issue
                WHERE id_copy = %s
        """, (idCopy,))
        return self.__cursor.fetchone()

    def InsertBookToAuthor(self, idBook, idAuthor):
        self.__cursor.execute("""
                INSERT INTO author_has_book (id_book, id_author) VALUES (%s, %s)
        """, (idBook, idAuthor))


    def UpdateAuthorBook(self, idAuthorNew, idBookNew, oldAuthorId):
        self.__cursor.execute("""
                UPDATE author_has_book SET id_book = %s, id_author = %s WHERE id_author = %s AND id_book = %s 
        """,
        (idBookNew, idAuthorNew, oldAuthorId, idBookNew))

    def CommitChanges(self):
        self.__connection.commit()


    def __del__(self):
        self.__cursor.close()
        self.__connection.close()