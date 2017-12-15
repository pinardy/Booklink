import MySQLdb as mdb

# ----------USER FUNCTIONS----------

def retrieveProfile(uid):
	'''
	:param uid: current user id
	:return: If there are no user profile - None. Else it returns a nested tuple of user profile
	'''
	con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
	with con:
		cur = con.cursor()

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
	'''
	:param uid: current user id
	:return: If there are no purchase history - None. Else it return a nested tuple of history transactions
	'''
	con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
	with con:
		cur = con.cursor()

		query = "SELECT * " \
				"FROM purchase_history,book " \
				"WHERE user_id = '{0}'" \
				"AND purchase_history.isbn13 = book.isbn13;".format(uid)
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
		
def getFeedbackHistory(uid):
	'''
	:param uid: current user id
	:return: If there are no feedback history - None. Else it returns a nested tuple of feedbacks
	'''
	con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
	with con:
		cur = con.cursor()
		
		query = "SELECT * " \
				"FROM feedback NATURAL JOIN (SELECT ISBN13,title FROM book) book " \
				"WHERE feedback_user = '{0}'" \
				"AND feedback.isbn13 = book.isbn13;".format(uid)
		cur.execute(query)
		if cur.rowcount == 0:
			print("No feedback history")
			return None
		else:
			print('User feedback history fetched')
			row = cur.fetchall()
			print(row)
			return row


def getRatingHistory(uid):
	'''
	:param uid: current user id
	:return: If there are no rating history - None. Else it returns a nested tuple of ratings
	Query: NATURAL JOIN over rating, book and rating.
	Returns fields ISBN13, feedback_user, rating_user, entry_date, score, title, feedback
	'''
	con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
	with con:
		cur = con.cursor()

		query = "SELECT * FROM( " \
				"SELECT * FROM rating " \
				"NATURAL JOIN (SELECT ISBN13,title FROM book) book " \
				"WHERE rating_user = '{0}') A NATURAL JOIN " \
				"(SELECT feedback_user,ISBN13,feedback FROM feedback) B;".format(uid)

		cur.execute(query)
		if cur.rowcount == 0:
			print("No Rating history")
			return None
		else:
			print('User feedback history fetched')
			row = cur.fetchall()
			print(row)
			return row