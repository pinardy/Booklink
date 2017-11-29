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

def PurchaseBook(orderlist):
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
        #Check all orders are within inventory limit first before subtracting
        for order in orderlist:
            query = "SELECT no_copies "\
            "FROM inventory " \
            "WHERE isbn13 = {0};".format(order[1])
            cur.execute(query)
            limit = cur.fetchall()
            if order[3] > limit[0][0]:
                return False #One of the orders has exceeded inventory

        #Update inventory
        for order in orderlist:
            query = "UPDATE inventory " \
                    "SET no_copies = no_copies - {0} " \
                    "WHERE isbn13 = {1};".format(order[3], order[1])
            cur.execute(query)
        return True

def SubmitPurchaseHistory(orderlist,username):
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
        cur.execute("SELECT max(purchase_id) FROM purchase_history;")
        last_purchaseid = cur.fetchall()[0][0]
        if last_purchaseid == None:
            last_purchaseid = 0
        else:
            last_purchaseid = int(last_purchaseid)
        now = datetime.datetime.now()

        for order in orderlist:
            last_purchaseid = last_purchaseid + 1
            print(last_purchaseid, username, order[1], order[3],now.strftime("%Y-%m-%d"))
            query = "INSERT into purchase_history VALUES "\
            "({0},'{1}','{2}',{3},'{4}');" .format(last_purchaseid, username, order[1], order[3],now.strftime("%Y-%m-%d"))
            cur.execute(query)