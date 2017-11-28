import MySQLdb as mdb

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

def getAllBookIsbnTitle():
	con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
	with con:
		cur = con.cursor()

		# TODO: Add price attribute to book
		query = "SELECT isbn13, title \
						FROM book"
		cur.execute(query)

		# No row exists
		if cur.rowcount == 0:
			print("No books in booklist")
			return
		else:
			row = cur.fetchall()
			return row