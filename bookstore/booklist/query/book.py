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

# Retrieve information on single book for book page
def getBook(isbn13):
	query = "SELECT * " \
			"FROM book " \
			"WHERE isbn13 = '{0}';".format(isbn13)
	return connectAndExecute(query)


# This is the conjunctive query
def getBooksByQuery(title='%', author='%', publisher='%', isbn13='%', order = '%', sort = '%' ):
	'''
	:param title: title of book
	:param author: author input
	:param publisher: publisher input
	:param isbn13: isbn13 input
	:param order: Year or Rating
	:param sort: ascending or descending
	:return: a nested tuple of books that matches the query
	'''
	query = "SELECT * FROM BOOK LEFT JOIN (SELECT isbn13, AVG(score) AS avgscore FROM feedback GROUP BY isbn13) AS B USING (ISBN13) " \
			"WHERE title LIKE '%{0}%'"\
			"AND authors LIKE '%{1}%'" \
			"AND isbn13 LIKE '%{2}%'"\
			"AND publisher LIKE '%{3}%'" \
			"ORDER BY {4} {5};".format(title,author,isbn13,publisher, order,sort)
	return connectAndExecute(query)


def getAllBookIsbnTitle():
	'''
	:return: tuple of book titles
	'''
	query = "SELECT isbn13, title \
			FROM book"
	return connectAndExecute(query)


# This is the recommender code
def recommendation(uid, isbn13):
	'''
	:param uid: current user id
	:param isbn13: the last book that the person has purchased
	:return: a suggested tuple of 3 books that is popular based on highest purchased
	Query:
	1st SELECT
	Aggregates the books based on the books bought buy people who bought the same book as the user
	Groups by isbn13 and returns top 3
	2nd SELECT
	Finds all distinct users that bought the same book as the user
	3rd SELECT
	Finds all the books that the user has already bought so that you will not recommend those books
	'''
	query = "SELECT isbn13, count(isbn13) " \
			"FROM purchase_history ph, " \
			"(SELECT DISTINCT user_id " \
			"FROM purchase_history ph " \
			"WHERE ph.ISBN13 = '{1}' AND ph.user_id != '{0}') AS T " \
			"WHERE ph.user_id = T.user_id AND ph.isbn13 " \
			"NOT IN " \
			"(SELECT DISTINCT isbn13 FROM purchase_history ph " \
			"WHERE ph.user_id = '{0}') " \
			"GROUP BY isbn13 " \
			"ORDER BY COUNT(isbn13) DESC " \
			"LIMIT 3;".format(uid,isbn13)

	return connectAndExecute(query)