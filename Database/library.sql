CREATE TABLE IF NOT EXISTS admin
(
    id_admin INT NOT NULL PRIMARY KEY,
    password BYTEA NOT NULL
);

CREATE TABLE IF NOT EXISTS student
(
    id_student INT NOT NULL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    birthday DATE NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL UNIQUE,
    password BYTEA NOT NULL
);

CREATE TABLE IF NOT EXISTS book
(
    id_book SERIAL NOT NULL PRIMARY KEY,
    isbn VARCHAR(13) NOT NULL,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS copy
(
    id_copy SERIAL NOT NULL PRIMARY KEY,
    id_book SERIAL NOT NULL,
    page_count INT NOT NULL,
    is_available SMALLINT NOT NULL,
    publisher VARCHAR(50),
    CONSTRAINT copy_book_id_book_fk
		FOREIGN KEY (id_book) 
			REFERENCES book(id_book)
				ON UPDATE CASCADE ON DELETE CASCADE
);

drop table copy cascade

CREATE TABLE IF NOT EXISTS author
(
    id_author SERIAL NOT NULL PRIMARY KEY,
    name VARCHAR(60) NOT NULL 
);

CREATE TABLE IF NOT EXISTS author_has_book
(
    id_author_has_book SERIAL NOT NULL PRIMARY KEY,
    id_author SERIAL NOT NULL,
    id_book SERIAL NOT NULL,
    CONSTRAINT author_has_book_book_id_book_fk
		FOREIGN KEY(id_book) 
			REFERENCES book(id_book)
				ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT author_has_book_author_id_author_fk
		FOREIGN KEY (id_author) 
			REFERENCES author(id_author)
				ON UPDATE CASCADE ON DELETE CASCADE      
);


CREATE TABLE IF NOT EXISTS issue 
(
    id_issue SERIAL NOT NULL PRIMARY KEY,
    id_student INT NOT NULL,
    id_copy INT NOT NULL,
    "start" DATE NOT NULL,
    "end" DATE NOT NULL,
    CONSTRAINT issue_student_id_student_fk
		FOREIGN KEY(id_student) 
			REFERENCES student(id_student)
				ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT issue_copy_id_copy_fk
		FOREIGN KEY (id_copy) 
			REFERENCES copy(id_copy)
				ON UPDATE CASCADE ON DELETE CASCADE   
);


SELECT copy.id_copy, book.name, author.name, start, "end" FROM student
INNER JOIN issue ON student.id_student = issue.id_student
INNER JOIN copy ON copy.id_copy = issue.id_copy
INNER JOIN book ON copy.id_book = book.id_book
INNER JOIN author_has_book on author_has_book.id_book = book.id_book
INNER JOIN  author ON author_has_book.id_author = author.id_author




insert into issue (id_student, id_copy, start, "end") values (1180501039, 1, '27-12-2020', '5-01-2021')


DELETE FROM copy WHERE id_copy = 2

drop table issue cascade
