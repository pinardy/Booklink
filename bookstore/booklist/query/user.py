import MySQLdb as mdb

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