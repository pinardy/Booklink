import MySQLdb as mdb

con = mdb.connect(host = "127.0.0.1", port=3306, user = "bookstore_user", passwd = "password", db = "bookstore")


with con:
    cur = con.cursor()

    # --- Schema ---
    book = "CREATE TABLE book (" \
           "title TINYTEXT NOT NULL," \
           "cover_format TINYTEXT CHECK(cover_format='paperback' or cover_format='hardcover')," \
           "num_pages INT," \
           "authors TINYTEXT," \
           "publisher TINYTEXT," \
           "year_publish INT," \
           "edition INT," \
           "ISBN10 CHAR(10) NOT NULL," \
           "ISBN13 CHAR(13) NOT NULL,PRIMARY KEY (ISBN13));"

    purchaseHistory = "CREATE TABLE purchase_history (" \
                      "purchase_id int(20) AUTO_INCREMENT," \
                      "user_id VARCHAR(20) NOT NULL," \
                      "ISBN13 CHAR(13) NOT NULL," \
                      "no_copies INT CHECK (no_copies > 0)," \
                      "order_date DATE NOT NULL," \
                      "PRIMARY KEY (purchase_id)," \
                      "FOREIGN KEY (user_id) REFERENCES auth_user(username)," \
                      "FOREIGN KEY (ISBN13) REFERENCES book (ISBN13));"

    inventory = "CREATE TABLE inventory(ISBN13 CHAR(13)," \
                "no_copies INT CHECK (no_copies > 0)," \
                "PRIMARY KEY (ISBN13)," \
                "FOREIGN KEY (ISBN13) REFERENCES book (ISBN13) ON DELETE CASCADE);"

    feedback = "CREATE TABLE feedback (" \
               "feedback_user VARCHAR(20)," \
               "ISBN13 CHAR(13)," \
               "order_date DATE NOT NULL," \
               "score INT CHECK (score >=0 AND score <= 10)," \
               "feedback TINYTEXT," \
               "PRIMARY KEY (feedback_user,ISBN13)," \
               "FOREIGN KEY (feedback_user) REFERENCES auth_user(username) ON DELETE CASCADE," \
               "FOREIGN KEY (ISBN13) REFERENCES book (ISBN13) ON DELETE CASCADE);"

    rating = "CREATE TABLE rating (" \
             "rating_user VARCHAR(20)," \
             "feedback_user VARCHAR(20)," \
             "ISBN13 CHAR(13)," \
             "entry_date DATE NOT NULL," \
             "score INT CHECK (score >=0 AND score <= 2)," \
             "PRIMARY KEY (feedback_user,rating_user,ISBN13)," \
             "FOREIGN KEY (rating_user) REFERENCES auth_user(username) ON DELETE CASCADE," \
             "FOREIGN KEY (feedback_user) REFERENCES feedback (feedback_user) ON DELETE CASCADE," \
             "FOREIGN KEY (ISBN13) REFERENCES book (ISBN13) ON DELETE CASCADE);"

    cart =  "CREATE TABLE cart (" \
            "ISBN13 CHAR(13)," \
            "username VARCHAR(150)," \
            "quantity int(8)," \
            "PRIMARY KEY (ISBN13,username)," \
            "FOREIGN KEY (ISBN13) REFERENCES book(ISBN13) ON DELETE CASCADE," \
            "FOREIGN KEY (username) REFERENCES auth_user(username) ON DELETE CASCADE);" \

    # Updates the inventory when a purchase is made
    updateInventory = "CREATE TRIGGER UpdateInventory " \
                      "AFTER INSERT on purchase_history " \
                      "FOR EACH Row " \
                      "UPDATE inventory " \
                      "SET inventory.no_copies = inventory.no_copies - NEW.no_copies " \
                      "WHERE inventory.ISBN13 = NEW.ISBN13;"

    # ========== TEST INSERTION SQL CODES =========

    # sql = "INSERT into books VALUES ('A Guide to the SQL Standard','paperback',240,'C.J. Date','Addison-Wesley',1989,2,'0201502097','978-0201502091');"

    # sql1 = "INSERT into books VALUES ('Database in Depth: Relational Theory for Practitioners',"\
    # 	  "'paperback',208,'C.J. Date','O''Reilly Media',2005,1,'0596100124','978-0596100124);"

    # sql2 = "INSERT into books VALUES ( 'Logic and Databases: The Roots of Relational Theory', 'paperback', 460, 'C.J. Date', 'Trafford Publishing', 2007, 1, '1425122906', '978-1425122904');"

    sql3 = "INSERT into books VALUES ('Database Management Systems'," \
           "'hardcover',454,'Michael M. Gorman','QED Information Sciences'," \
           "1991,1,'0894353233','978-0894353239');"

    # ============================================
    try:
        cur.execute(book)
        print("Created book table")
    except:
        print("EXCEPTION: Created book table")

    try:
        cur.execute(purchaseHistory)
        print("Created purchaseHistory table")
    except:
        print("EXCEPTION: Created purchaseHistory table")

    try:
        cur.execute(inventory)
        print("Created inventory table")
    except:
        print("EXCEPTION: Created inventory table")

    try:
        cur.execute(feedback)
        print("Created feedback table")
    except:
        print("EXCEPTION: Created feedback table")

    try:
        cur.execute(rating)
        print("Created rating table")
    except:
        print("EXCEPTION: Created rating table")

    try:
        cur.execute(cart)
        print("Created cart table")
    except:
        print("EXCEPTION: Created cart table")

    try:
        cur.execute(updateInventory)
        print("Created inventory trigger")
    except:
        print("EXCEPTION: Created inventory trigger")

    print("--- Execution of SQL successful ---")