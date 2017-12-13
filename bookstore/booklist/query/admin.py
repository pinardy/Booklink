import MySQLdb as mdb
import datetime

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

# ----------ADMIN FUNCTIONS----------

def insertBook(title, authors, publisher, year_publish, cost, isbn10, isbn13, quantity):
	con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
	with con:
		cur = con.cursor()

		query = "INSERT into book VALUES" \
				"('{0}','{1}','{2}','{3}','{4}'," \
				"'{5}','{6}');".format(title, authors, publisher, year_publish, cost, isbn10, isbn13)

		cur.execute(query)
		
		query = "INSERT into inventory VALUES" \
				"('{0}',{1});".format(isbn13,quantity)
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
				"SET no_copies = '{0}' " \
				"WHERE isbn13 = '{1}';".format(newStock, isbn13)
		cur.execute(query)
		return True

def getHighestCopies(month, year, m):
	query = "SELECT book.title,SUM(no_copies) " \
			"from purchase_history,book " \
			"WHERE MONTH(purchase_history.order_date) = {0} " \
			"AND YEAR(purchase_history.order_date) = {1} " \
			"AND book.ISBN13 = purchase_history.ISBN13 " \
			"GROUP BY purchase_history.ISBN13 " \
			"ORDER BY SUM(no_copies) DESC " \
			"LIMIT {2};".format(month, year, m)
	return connectAndExecute(query)


def getHighestPublishers(month, year, m):
	query = "SELECT b.publisher, SUM(no_copies) " \
			"FROM purchase_history ph, book b " \
			"WHERE MONTH(ph.order_date) = {0} " \
			"AND YEAR(ph.order_date) = {1} " \
			"AND b.ISBN13 = ph.ISBN13 " \
			"GROUP BY b.publisher " \
			"ORDER BY SUM(no_copies) DESC " \
			"LIMIT {2};".format(month, year, m)
	return connectAndExecute(query)


def getHighestAuthors(month, year, m):
	query = "SELECT b.authors, SUM(no_copies) " \
			"FROM purchase_history ph, book b " \
			"WHERE MONTH(ph.order_date) = {0} " \
			"AND YEAR(ph.order_date) = {1} " \
			"AND b.ISBN13 = ph.ISBN13 " \
			"GROUP BY b.authors " \
			"ORDER BY SUM(no_copies) DESC " \
			"LIMIT {2};".format(month, year, m)
	return connectAndExecute(query)


def getStatistics(choices, m):
	d = datetime.date.today()

	if choices == 'book':
		return (('Title', 'Count'),) + getHighestCopies(d.month, d.year, m)

	elif choices == 'authors':
		return (('Author(s)', 'Count'),) + getHighestAuthors(d.month, d.year, m)

	elif choices == 'publisher':
		return (('Publisher', 'Count'),) + getHighestPublishers(d.month, d.year, m)
