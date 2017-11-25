import MySQLdb as mdb

# ----------BOOK FUNCTIONS----------

# Retrieve information on all books to display on homepage
def getAllBooks():
	con = mdb.connect(host = "127.0.0.1", port=3306, user = "bookstore_user", passwd = "password", db = "bookstore")
	with con:
		cur = con.cursor()
		
		# TODO: Add price attribute to book
		query = "SELECT title, authors \
				FROM book"
		cur.execute(query)
		
		# No row exists
		if cur.rowcount == 0:
			print("No books in booklist")
			return
		else:
			row = cur.fetchall()
			return row

def insertBook(title,cover_format,num_pages,authors,publisher,year_publish,edition,isbn10,isbn13):
	con = mdb.connect(host = "127.0.0.1", port=3306, user = "bookstore_user", passwd = "password", db = "bookstore")
	with con:
		cur = con.cursor()
		"""
		#query = "INSERT INTO book \
				#VALUES({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})".format(title, cover_format, num_pages, authors, publisher, year_publish, edition, isbn10, isbn13)
		#query = "INSERT into book VALUES ('Database Management Systems'," \
				#"'hardcover',454,'Michael M. Gorman','QED Information Sciences'," \
				#"1991,1,'0894353233','9780894353239');"
				
		title = 'Database Management Systems (test)'
		cover_format = 'hardcover'
		num_pages = 454
		authors = 'Michael M. Gorman'
		publisher = 'QED Information Sciences'
		year_publish = 1991
		edition = 1
		isbn10 = '0894353233'
		isbn13 = '9780894353239';
		"""
				
		query = "INSERT into book VALUES ('{0}'," \
				"'{1}',{2},'{3}','{4}'," \
				"{5},{6},'{7}','{8}');".format(title, cover_format, num_pages, authors, publisher, year_publish, edition, isbn10, isbn13)
		cur.execute(query)

def deleteBook(isbn13):
	con = mdb.connect(host = "127.0.0.1", port=3306, user = "bookstore_user", passwd = "password", db = "bookstore")
	with con:
		cur = con.cursor()
		
		query = "DELETE from book WHERE isbn10 = '{0}';".format(isbn13)
		cur.execute(query)
		
# Retrieve information on single book for book page
def getBook(isbn13):
	con = mdb.connect(host = "127.0.0.1", port=3306, user = "bookstore_user", passwd = "password", db = "bookstore")
	with con:
		cur = con.cursor()
		
		query = "SELECT * FROM book WHERE isbn13 = '{0}';".format(isbn13)
		cur.execute(query)
		
		# No row exists
		if cur.rowcount == 0:
			print("No such book exists")
			return
		else:
			row = cur.fetchall()
			return row

def setInventory(isbn13, initStock):
	con = mdb.connect(host = "127.0.0.1", port=3306, user = "bookstore_user", passwd = "password", db = "bookstore")
	with con:
		cur = con.cursor()
		
		query = "INSERT into inventory('{0}','{1}');".format(isbn13, initStock)
		
def getInventory(isbn13):
	con = mdb.connect(host = "127.0.0.1", port=3306, user = "bookstore_user", passwd = "password", db = "bookstore")
	with con:
		cur = con.cursor()
		
		query = "SELECT * FROM book WHERE isbn13 = '{0}';".format(isbn13)
		cur.execute(query)
		
		# No row exists
		if cur.rowcount == 0:
			print("No such inventory exists")
			return
		else:
			row = cur.fetchall()
			return row

def updateInventory(isbn13, newStock):
	con = mdb.connect(host = "127.0.0.1", port=3306, user = "bookstore_user", passwd = "password", db = "bookstore")
	with con:
		cur = con.cursor()
		
		query = "UPDATE inventory" \
				"SET no_copies = {0}" \
				"WHERE isbn13 = {1}".format(newStock, isbn13)
				
# ----------USER FUNCTIONS----------