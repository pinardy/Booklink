import MySQLdb as mdb
import datetime

def addToCart(isbn13, username, quantity):
    '''
    :param isbn13: single book isbn13 to add to cart
    :param username: logged in user
    :param quantity: how many of that book to add to cart
    :return: None, insert values into cart
    '''
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
        query = "INSERT INTO cart VALUES "\
        "('{0}','{1}',{2});".format(isbn13, username, quantity)
        cur.execute(query)

def delFromCart(isbn13, username):
    '''
    :param isbn13: single book isbn13 to delete from cart
    :param username: logged in user
    :return: None, delete book entirely from cart
    '''
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
        query = "DELETE FROM cart "\
        "WHERE isbn13 = '{0}' and username = '{1}';".format(isbn13, username)
        cur.execute(query)

def delAllFromCart(username):
    '''
    :param username: logged in user
    :return: None, delete user's cart entirely
    '''
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
        query = "DELETE FROM cart "\
        "WHERE username = '{0}';".format(username)
        cur.execute(query)

def modifyCart(isbn13, username, newquantity):
    '''
    :param isbn13: single book isbn13 currently in cart to modify
    :param username: logged in user
    :param newquantity: specify the new quantity to update (not addition, update)
    :return: None, updates the user's specified book quantity in his cart
    '''
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
        query = "UPDATE cart "\
        "SET quantity = {2} " \
        "WHERE isbn13 = '{0}' and username = '{1}';".format(isbn13, username, newquantity)
        cur.execute(query)

def showCart(username):
    '''
    :param username: logged in user
    :return: nested list of user's cart
    Query: Inner subquery - join cart, inventory and book tables
    '''
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
    '''
    :param username: logged in user
    :return: rows for books in the cart whose quantity exceeds its inventory, else None
    '''
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
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
    :param username: logged in user
    :return: True if query succeeds, insert values from cart into purchase_history
    '''
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
        now = datetime.datetime.now()
        #Check all orders are within inventory limit first before subtracting
        query = "INSERT INTO purchase_history (purchase_id, user_id, ISBN13, no_copies, order_date) " \
                "SELECT null, username, isbn13, quantity, '{0}' FROM cart " \
                "WHERE cart.username = '{1}';".format(now.strftime("%Y-%m-%d"),username)

        cur.execute(query)
        return True