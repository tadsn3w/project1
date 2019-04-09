CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_login VARCHAR (10) NOT NULL,
    user_name VARCHAR (100) NOT NULL,
    user_email VARCHAR(100)  NOT NULL,
    user_password VARCHAR(20) NOT NULL
);

CREATE TABLE books (
    isbn VARCHAR (10) PRIMARY KEY,
    title VARCHAR (50) NOT NULL,
    author VARCHAR(50) NOT NULL,
    published INTEGER NOT NULL
);

CREATE TABLE reviews (
    user_id INTEGER NOT NULL,
    isbn VARCHAR(10) NOT NULL,
    rating integer NOT NULL,
    comment TEXT, 
    PRIMARY KEY (user_id,isbn)  
);