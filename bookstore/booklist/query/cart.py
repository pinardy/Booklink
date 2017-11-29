import MySQLdb as mdb

def addToCart(isbn13, username, quantity):
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
        query = "INSERT INTO cart VALUES "\
        "('{0}','{1}',{2});".format(isbn13, username, quantity)
        cur.execute(query)

def delFromCart(isbn13, username):
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
        query = "DELETE FROM cart "\
        "WHERE isbn13 = '{0}' and username = '{1}';".format(isbn13, username)
        cur.execute(query)

def delAllFromCart(username):
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
        query = "DELETE FROM cart "\
        "WHERE username = '{0}';".format(username)
        cur.execute(query)

def modifyCart(isbn13, username, newquantity):
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
        query = "UPDATE cart "\
        "SET quantity = {2} " \
        "WHERE isbn13 = '{0}' and username = '{1}';".format(isbn13, username, newquantity)
        cur.execute(query)

def showCart(username):
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()

        query = "SELECT b.title, c.quantity "\
        "FROM book b, cart c "\
        "WHERE b.ISBN13 = c.ISBN13 "\
        "AND c.username = '{0}'".format(username)
        cur.execute(query)

        # No row exists
        if cur.rowcount == 0:
            print("No item in cart")
            return None
        else:
            print('User profile fetched')
            row = cur.fetchall()
            print(row)
            return row