import MySQLdb as mdb

con = mdb.connect(host = "localhost", user = "root", passwd = "123456", db = "onlineBookStore")

with con:
	cur = con.cursor()

	#TODO: Write Schema here
	cur.execute("CREATE TABLE < SQL code here >")

