SELECT * FROM student WHERE id_student = 1180501039;

SELECT * FROM admin WHERE id_admin = 1;

SELECT author.name FROM author
INNER JOIN author_has_book on author.id_author = author_has_book.id_author
INNER JOIN book on book.id_book = author_has_book.id_book
WHERE isbn = '1912829312312';

--2
SELECT isbn FROM book
INNER JOIN author_has_book on book.id_book = author_has_book.id_book
INNER JOIN author on author.id_author = author_has_book.id_author
WHERE author.id_author = 13 AND book.name = 'Тихий дон';

CREATE INDEX IX_author_has_book_id_author
ON author_has_book(id_author);

CREATE INDEX IX_book_isbn
ON book(isbn);

--3

SELECT author.name, book.name, copy.id_copy, start, "end" FROM student
INNER JOIN issue ON student.id_student = issue.id_student
INNER JOIN copy ON copy.id_copy = issue.id_copy
INNER JOIN book ON copy.id_book = book.id_book
INNER JOIN author_has_book on author_has_book.id_book = book.id_book
INNER JOIN  author ON author_has_book.id_author = author.id_author
WHERE copy.is_available = 0 AND student.id_student = 1180501039;

CREATE INDEX IX_issue_id_student
ON issue(id_student);

CREATE INDEX IX_copy_id_book
ON copy(id_book);

--4
SELECT temp.id_book, temp.name, author.name, copyCount, temp.page_count, temp.publisher FROM
(SELECT book.id_book, book.isbn, book.name, count(book.id_book) as copyCount, page_count, publisher FROM book
INNER JOIN copy on book.id_book = copy.id_book
INNER JOIN author_has_book on author_has_book.id_book = book.id_book
INNER JOIN author on author.id_author = author_has_book.id_author
WHERE book.name = 'Тихий дон' and is_available = 1
GROUP BY book.id_book, publisher, page_count) AS temp
INNER JOIN author_has_book on temp.id_book = author_has_book.id_book
INNER JOIN author on author.id_author = author_has_book.id_author;

--5
SELECT temp.id_book, temp.name, author.name, copyCount, temp.page_count, temp.publisher FROM
(SELECT book.id_book, book.isbn, book.name, count(book.id_book) as copyCount, page_count, publisher FROM author
INNER JOIN author_has_book on author.id_author = author_has_book.id_author
INNER JOIN book on book.id_book = author_has_book.id_book
INNER JOIN copy on book.id_book = copy.id_book
WHERE author.name = 'Шолохов' and is_available = 1
GROUP BY book.id_book, publisher, page_count
) AS temp
INNER JOIN author_has_book on temp.id_book = author_has_book.id_book
INNER JOIN author on author.id_author = author_has_book.id_author;

--6


SELECT book_name FROM author
INNER JOIN author_has_book ON author.id_author = author_has_book.id_author
INNER JOIN
(SELECT id_book,name AS book_name FROM book) AS book
ON book.id_book = author_has_book.id_book
WHERE name = 'Шолохов';

CREATE INDEX IX_author_name
ON author(name);

--7
SELECT id_copy FROM copy
INNER JOIN (SELECT id_book, isbn, name FROM book) AS book ON book.id_book = copy.id_book
WHERE name = 'Тихий дон' AND is_available = 1;

--8
SELECT first_name, last_name, birthday, email, phone FROM student WHERE id_student = 1180501039;

CREATE INDEX IX_student_info
ON student(id_student)
INCLUDE(first_name, last_name, birthday, email, phone);

--9
SELECT id_student FROM student WHERE phone = '89021089168';

--10
SELECT id_student FROM student WHERE email = 'a@mail.ru';

--11
SELECT id_student FROM student WHERE id_student = 1180501039;

--12
SELECT name FROM author WHERE name = 'Шолохов';


CREATE INDEX IX_student_info
ON student(id_student)
INCLUDE(first_name, last_name, birthday, email, phone);

CREATE INDEX IX_author_has_book_id_author
ON author_has_book(id_author);

CREATE INDEX IX_issue_id_student
ON issue(id_student);

CREATE INDEX IX_copy_id_book
ON copy(id_book);

CREATE INDEX IX_author_name
ON author(name);



