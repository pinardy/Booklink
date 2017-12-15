import MySQLdb as mdb
import datetime

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
        query = "SELECT b.title, a.* FROM( "\
            "SELECT * FROM cart "\
        "NATURAL JOIN inventory) as a "\
        "NATURAL JOIN book b "\
        "WHERE a.username = '{0}';".format(username)
        cur.execute(query)

        if cur.rowcount == 0:
            return None
        else:
            row = cur.fetchall()
            return row

def ValidPurchase(username):
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
        # This query returns something if there are items on the cart that exceeds inventory
        # else it returns nothing
        query = "SELECT * FROM INVENTORY, cart " \
                "WHERE cart.isbn13 = inventory.isbn13 " \
                "and cart.username = '{0}' " \
                "and no_copies < quantity;".format(username)

        cur.execute(query)

        if cur.rowcount == 0:

            return None
        else:
            row = cur.fetchall()
            return row

def PurchaseBook(username):
    '''
    :param username: takes in current user
    :return: True to indicate that the query run successful
    Query: Submits a purchase_history based on contents on cart
    '''
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
        now = datetime.datetime.now()
        #Check all orders are within inventory limit first before subtracting
        query = "INSERT INTO purchase_history (purchase_id, user_id, ISBN13, no_copies, order_date) " \
                "SELECT null, username, isbn13, quantity, '{0}' FROM cart " \
                "WHERE cart.username = '{1}';".format(now.strftime("%Y-%m-%d"), username)
        print(query)
        cur.execute(query)
        return True