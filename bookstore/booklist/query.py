import MySQLdb as mdb
import sys

# TODO: Add ID for purchaseBook()

# ----------BOOK FUNCTIONS----------

# Retrieve information on all books to display on homepage
def getAllBooks():
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()

        # TODO: Add price attribute to book
        query = "SELECT * " \
				"FROM book;"
        cur.execute(query)

        # No row exists
        if cur.rowcount == 0:
            print("No books in booklist")
            return
        else:
            row = cur.fetchall()
            return row

# Retrieve information on single book for book page
def getBook(isbn13):
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()

        query = "SELECT * " \
				"FROM book " \
				"WHERE isbn13 = '{0}';".format(isbn13)
        cur.execute(query)

        # No row exists
        if cur.rowcount == 0:
            print("No such book exists")
            return
        else:
            row = cur.fetchall()
            return row


def setInventory(isbn13, initStock):
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()

        query = "INSERT into inventory VALUES" \
				"('{0}',{1});".format(isbn13, initStock)
        cur.execute(query)
        return True

def getInventory(isbn13):
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()

        query = "SELECT no_copies " \
				"FROM inventory " \
				"WHERE isbn13 = '{0}';".format(isbn13)
        cur.execute(query)

        # No row exists
        if cur.rowcount == 0:
            print("No such inventory exists")
            return
        else:
            row = cur.fetchall()
            return row
				
def purchaseBook(uid, isbn13, no_copies, date):
	con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
	with con:
		cur = con.cursor()
		
		#TODO: Add ID
		query = "INSERT into purchase_history VALUES" \
				"('SomeID','{0}','{1}',{2},'{3}');".format(uid, isbn13, no_copies, date)
		cur.execute(query)
		return True


def bookRating(isbn13):
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
		
        query = "SELECT AVG(score) " \
				"FROM feedback " \
				"WHERE isbn13 = {0};".format(isbn13)
        cur.execute(query)
		
		# No row exists
        if cur.rowcount == 0:
            print("No book rating")
            return
        else:
            print('Book rating fetched')
            row = cur.fetchall()[0][0]
            if(bool(row==None)):
                print('No rating had been given')
                return 0;
            else:
                print('Rating fetched')
                print(row)
                return row
		
def getBookFeedback(isbn13):
	con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
	with con:
		cur = con.cursor()
		
		query = "SELECT * " \
				"FROM feedback " \
				"WHERE isbn13 = {0};".format(isbn13)
		cur.execute(query)
		
		# No row exists
        if cur.rowcount == 0:
            print("No feedback exists")
            return
        else:
            row = cur.fetchall()
            return row

# ----------ADMIN FUNCTIONS----------	
		
def insertBook(title, cover_format, num_pages, authors, publisher, year_publish, edition, isbn10, isbn13, inventory):
	con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
	with con:
		cur = con.cursor()

		query = "INSERT into book VALUES" \
                "('{0}','{1}',{2},'{3}','{4}'," \
                "{5},{6},'{7}','{8}');".format(title, cover_format, num_pages, authors, publisher, year_publish, edition, isbn10, isbn13)
				
				
		cur.execute(query)
		
		query = "INSERT into inventory VALUES" \
				"('{0}',{1});".format(isbn13,inventory)		
		cur.execute(query)
		return True

def deleteBook(isbn13):
	con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
	with con:
		cur = con.cursor()

		query = "DELETE FROM book " \
				"WHERE isbn13 = '{0}';".format(isbn13)
		cur.execute(query)
		return True
		
def updateInventory(isbn13, newStock):
	con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
	with con:
		cur = con.cursor()

		query = "UPDATE inventory " \
                "SET no_copies = {0} " \
                "WHERE isbn13 = {1};".format(newStock, isbn13)
		cur.execute(query)
		return True
		
# ----------USER FUNCTIONS----------

def retrieveProfile(uid):
	con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
	with con:
		cur = con.cursor()

		# TODO: Add price attribute to book
		query = "SELECT * " \
                "FROM auth_user " \
                "WHERE username = '{0}';".format(uid)
		cur.execute(query)

        # No row exists
		if cur.rowcount == 0:
			print("No user profile")
			return None
		else:
			print('User profile fetched')
			row = cur.fetchall()
			print(row)
			return row

def getPurchaseHistory(uid):
	con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
	with con:
		cur = con.cursor()
		
		query = "SELECT * " \
				"FROM purchase_history " \
				"WHERE user_id = '{0}';".format(uid)
		cur.execute(query)
		
		# No row exists
		if cur.rowcount == 0:
			print("No purchase history")
			return None
		else:
			print('User purchase history fetched')
			row = cur.fetchall()
			print(row)
			return row
			
def feedbackBook(uid, isbn13, date, score, feedback):
	con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
	with con:
		cur = con.cursor()
		
		query = "INSERT into feedback VALUES" \
				"('{0}','{1}','{2}',{3},'{4}');".format(uid, isbn13, date, score, feedback)
		cur.execute(query)
		return True
		
def getFeedbackHistory(uid):
	con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
	with con:
		cur = con.cursor()
		
		query = "SELECT * " \
				"FROM feedback " \
				"WHERE feedback_user = '{0}';".format(uid)
		cur.execute(query)
		if cur.rowcount == 0:
			print("No feedback history")
			return None
		else:
			print('User feedback history fetched')
			row = cur.fetchall()
			print(row)
			return row
		
def rateUser(rating_user, feedback_user, isbn13, date, score,):
	con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
	with con:
		cur = con.cursor()
		
		query = "INSERT into rating VALUES" \
				"('{0}','{1}','{2}','{3}',{4});".format(rating_user, feedback_user, isbn13, date, score,)
		cur.execute(query)
		return True

def userRating(uid):
	con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
	with con:		
		cur = con.cursor()
		
		query = "SELECT AVG(score) " \
				"FROM rating " \
				"WHERE feedback_user = '{0}';".format(uid)
		cur.execute(query)
		
		# No row exists
		if cur.rowcount == 0:
			print("No user profile")
			return
		else:
			print('User profile fetched')
			row = cur.fetchall()[0][0]
			if(bool(row==None)):
				print('No rating had been given')
				return 0;
			else:
				print('Rating fetched')
				print(row)
				return row