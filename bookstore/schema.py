import MySQLdb as mdb

con = mdb.connect(host = "127.0.0.1", port=3306, user = "bookstore_user", passwd = "password", db = "bookstore")


with con:
    cur = con.cursor()

    #TODO: Write Schema here
    # creates the user account
    userAccount = "CREATE TABLE user_account(" \
                  "user_id VARCHAR(20)," \
                  "login_name VARCHAR(20) UNIQUE," \
                  "user_password VARCHAR(20) NOT NULL," \
                  "feedback TINYTEXT," \
                  "PRIMARY KEY(user_id));"

    purchaseHistory = "CREATE TABLE purchase_history (" \
                      "purchase_id VARCHAR(20)," \
                      "user_id VARCHAR(20) NOT NULL," \
                      "ISBN13 CHAR(13) NOT NULL," \
                      "no_copies INT CHECK (no_copies > 0)," \
                      "order_date DATE NOT NULL," \
                      "PRIMARY KEY (purchase_id)," \
                      "FOREIGN KEY (user_id) REFERENCES user_account(user_id)," \
                      "FOREIGN KEY (ISBN13) REFERENCES book (ISBN13));"

    inventory = "CREATE TABLE inventory(ISBN13 CHAR(13)," \
                "no_copies INT CHECK (no_copies > 0)," \
                "PRIMARY KEY (ISBN13)," \
                "FOREIGN KEY (ISBN13) REFERENCES book (ISBN13) ON DELETE CASCADE);"

    feedback = "CREATE TABLE feedback (" \
               "feedback_user VARCHAR(20)," \
               "ISBN13 CHAR(13)," \
               "order_date DATE NOT NULL," \
               "PRIMARY KEY (feedback_user,ISBN13)," \
               "FOREIGN KEY (feedback_user) REFERENCES user_account(user_id) ON DELETE CASCADE," \
               "FOREIGN KEY (ISBN13) REFERENCES book (ISBN13) ON DELETE CASCADE);"

    rating = "CREATE TABLE rating (" \
             "rating_user VARCHAR(20)," \
             "feedback_user VARCHAR(20)," \
             "ISBN13 CHAR(13)," \
             "entry_date DATE NOT NULL," \
             "PRIMARY KEY (feedback_user,rating_user,ISBN13)," \
             "FOREIGN KEY (rating_user) REFERENCES user_account(user_id) ON DELETE CASCADE," \
             "FOREIGN KEY (feedback_user) REFERENCES feedback (feedback_user) ON DELETE CASCADE," \
             "FOREIGN KEY (ISBN13) REFERENCES book (ISBN13) ON DELETE CASCADE);"

    # ========== TEST INSERTION SQL CODES =========

    # sql = "INSERT into books VALUES ('A Guide to the SQL Standard','paperback',240,'C.J. Date','Addison-Wesley',1989,2,'0201502097','978-0201502091');"

    # sql1 = "INSERT into books VALUES ('Database in Depth: Relational Theory for Practitioners',"\
    # 	  "'paperback',208,'C.J. Date','O''Reilly Media',2005,1,'0596100124','978-0596100124);"

    # sql2 = "INSERT into books VALUES ( 'Logic and Databases: The Roots of Relational Theory', 'paperback', 460, 'C.J. Date', 'Trafford Publishing', 2007, 1, '1425122906', '978-1425122904');"

    sql3 = "INSERT into books VALUES ('Database Management Systems'," \
           "'hardcover',454,'Michael M. Gorman','QED Information Sciences'," \
           "1991,1,'0894353233','978-0894353239');"

    # ============================================

    # Execution of cursor objects for schema
    try:
        cur.execute(userAccount)
        print("Created userAccount table")
    except:
        print("userAccount already exists")

    #TODO: Fix the remaining of the schema
    cur.execute(purchaseHistory)
    print("Created purchaseHistory table")

    cur.execute(inventory)
    print("Created inventory table")

    cur.execute(feedback)
    print("Created feedback table")

    cur.execute(rating)
    print("Created rating table")

    print("--- Execution of SQL successful ---")

