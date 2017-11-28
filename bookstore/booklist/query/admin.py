import MySQLdb as mdb

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