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
    publisher VARCHAR(50),
    CONSTRAINT copy_book_id_book_fk
		FOREIGN KEY (id_book) 
			REFERENCES book(id_book)
				ON UPDATE CASCADE ON DELETE CASCADE
);

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






