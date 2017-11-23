import MySQLdb as mdb

con = mdb.connect(host = "127.0.0.1", port=3306, user = "bookstore_user", passwd = "password", db = "bookstore")


with con:
	cur = con.cursor()

	#TODO: Write Schema here
	# sql = "INSERT into books VALUES ('A Guide to the SQL Standard','paperback',240,'C.J. Date','Addison-Wesley',1989,2,'0201502097','978-0201502091');"
	sql = "INSERT into books VALUES ('Database in Depth: Relational Theory for Practitioners','paperback',208,'C.J. Date','O''Reilly Media',2005,1,'0596100124','978-0596100124);"

	# Execute the cursor object to create schema
	cur.execute(sql)

