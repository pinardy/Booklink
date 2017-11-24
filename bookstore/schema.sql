# Create the database and user/password
create database bookstore;
create user bookstore_user identified by 'password';
grant all on bookstore.* to 'bookstore_user'@'%';
flush privileges;


CREATE TABLE Books (
    title VARCHAR(128) NOT NULL,
    format VARCHAR(128), 
    pages INTEGER,
    authors VARCHAR(128),
    publisher VARCHAR(128),
    year INTEGER,
    edition VARCHAR(128),
    ISBN10 CHAR(10) NOT NULL UNIQUE,
    ISBN13 CHAR(14) NOT NULL,
    PRIMARY KEY(ISBN10),
    CHECK(format='paperback' OR format='hardcover')
);


# creates the user account
CREATE TABLE user_account (
	user_id VARCHAR(20),
    login_name VARCHAR(20) UNIQUE,
    user_password VARCHAR(20) NOT NULL,
    feedback TINYTEXT,
    PRIMARY KEY (user_id)
);

# Order and Purchases combined into 1 table
CREATE TABLE purchase_history (
    purchase_id VARCHAR(20),
    user_id VARCHAR(20) NOT NULL,
    ISBN13 CHAR(13) NOT NULL,
    no_copies INT CHECK (no_copies > 0),
    order_date DATE NOT NULL, # check do we need this?
    PRIMARY KEY (purchase_id),
    FOREIGN KEY (user_id) REFERENCES user_account(user_id),
    FOREIGN KEY (ISBN13) REFERENCES book (ISBN13)
);

# Keeps track of the number of copies
CREATE TABLE inventory(
	ISBN13 CHAR(13),
    no_copies INT CHECK (no_copies > 0),
    PRIMARY KEY (ISBN13),
    FOREIGN KEY (ISBN13) REFERENCES book (ISBN13) ON DELETE CASCADE
);

# Feedback for the Book
# Check do we need a feedback_id, could we use user_id,ISBN13 as the key instead? JJJ - I am more in favour of using user_id,ISBN13
CREATE TABLE feedback (
    feedback_user VARCHAR(20),
    ISBN13 CHAR(13),
    order_date DATE NOT NULL, # CHECK do we need this?
    PRIMARY KEY (feedback_user,ISBN13),
    FOREIGN KEY (feedback_user) REFERENCES user_account(user_id) ON DELETE CASCADE,
    FOREIGN KEY (ISBN13) REFERENCES book (ISBN13) ON DELETE CASCADE
);

# Rating for the Feedback
# Check do we need a rating_id, could we use feedback_id,user_id as the key instead? JJJ - I am more in favour of using feedback_user,rating_user,ISBN13
CREATE TABLE rating (
	rating_user VARCHAR(20),
    feedback_user VARCHAR(20),
    ISBN13 CHAR(13),
    entry_date DATE NOT NULL, # CHECK do we need this?
    PRIMARY KEY (feedback_user,rating_user,ISBN13),
    FOREIGN KEY (rating_user) REFERENCES user_account(user_id) ON DELETE CASCADE,
    FOREIGN KEY (feedback_user) REFERENCES feedback (feedback_user) ON DELETE CASCADE,
    FOREIGN KEY (ISBN13) REFERENCES book (ISBN13) ON DELETE CASCADE
);