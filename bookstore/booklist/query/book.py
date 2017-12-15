import MySQLdb as mdb

def connectAndExecute(query):
	con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
	with con:
		cur = con.cursor()
		cur.execute(query)

		if cur.rowcount == 0:
			print("No books in booklist")
			return
		else:
			row = cur.fetchall()
			return row


# ----------BOOK FUNCTIONS----------

# Retrieve information on all books to display on homepage
def getAllBooks():
	query = "SELECT * " \
			"FROM book;"
	return connectAndExecute(query)


# Retrieve information on single book for book page
def getBook(isbn13):
	query = "SELECT * " \
			"FROM book " \
			"WHERE isbn13 = '{0}';".format(isbn13)
	return connectAndExecute(query)


def searchBookByTitle(title):
	query = "SELECT * " \
				"FROM book " \
				"WHERE title LIKE '%{0}%';".format(title)
	return connectAndExecute(query)


def setInventory(isbn13, initStock):
	con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
	with con:
		cur = con.cursor()

		query = "INSERT into inventory VALUES" \
				"('{0}',{1});".format(isbn13, initStock)
		cur.execute(query)
		return True

def getInventory(isbn13):
	query = "SELECT no_copies " \
			"FROM inventory " \
			"WHERE isbn13 = '{0}';".format(isbn13)
	return connectAndExecute(query)


def purchaseBook(uid, isbn13, no_copies, date):
	con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
	with con:
		cur = con.cursor()

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
				"WHERE isbn13 = '{0}';".format(isbn13)
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
	query = "SELECT * " \
			"FROM feedback " \
			"WHERE isbn13 = '{0}';".format(isbn13)
	return connectAndExecute(query)

def getBooksByQuery(title='%', author='%', publisher='%', isbn13='%', order = '%', sort = '%' ):
	query = "SELECT * FROM BOOK LEFT JOIN (SELECT isbn13, AVG(score) AS avgscore FROM feedback GROUP BY isbn13) AS B USING (ISBN13) " \
			"WHERE title LIKE '%{0}%'"\
			"AND authors LIKE '%{1}%'" \
			"AND isbn13 LIKE '%{2}%'"\
			"AND publisher LIKE '%{3}%'" \
			"ORDER BY {4} {5};".format(title,author,isbn13,publisher, order,sort)
	return connectAndExecute(query)



def getAllBookIsbnTitle():
	query = "SELECT isbn13, title \
			FROM book"
	return connectAndExecute(query)

def recommendation(uid, isbn13):
	query = "SELECT isbn13, count(isbn13) " \
			"FROM purchase_history ph, " \
			"(SELECT DISTINCT user_id " \
			"FROM purchase_history ph " \
			"WHERE ph.ISBN13 = '{1}' AND ph.user_id != '{0}') " \
			"AS T WHERE ph.user_id = T.user_id AND ph.isbn13 " \
			"NOT IN " \
			"(SELECT DISTINCT isbn13 FROM purchase_history ph " \
			"WHERE ph.user_id = '{0}') " \
			"GROUP BY isbn13 " \
			"ORDER BY COUNT(isbn13) DESC " \
			"LIMIT 3;".format(uid,isbn13)

	return connectAndExecute(query)