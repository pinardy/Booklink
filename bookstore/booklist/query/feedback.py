import MySQLdb as mdb
import datetime

def userHasGivenFeedback(isbn13,username):
    '''
    Returns True if user has given feedback for particular book.
    '''
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
        query = "SELECT * " \
                "FROM feedback " \
                "WHERE feedback_user = '{0}' and isbn13 = {1};".format(username, isbn13)
        cur.execute(query)
        if cur.rowcount == 0:
            return None
        else:
            row = cur.fetchall()
            return row

def writeFeedback(isbn13,username,score,text):
    '''
    Returns True if user has given feedback for particular book.
    '''
    if userHasGivenFeedback(isbn13, username) is not None:
        return False

    else:
        con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
        with con:
            cur = con.cursor()
            query = "INSERT INTO feedback VALUES " \
                    "('{0}',{1},{2},'{3}');".format(username, isbn13, score, text)
            cur.execute(query)
        rateFeedback(isbn13, 'admin', username, 0) #Initialize an admin rating of 0, so it can appear in testimonial

def userHasRateFeedback(isbn13,rating_username,feedback_username):
    '''
    Returns True if user has given feedback for particular book.
    '''
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
        query = "SELECT * " \
                "FROM rating " \
                "WHERE rating_user = '{0}' and feedback_user = '{1}' and isbn13 = {2};".format(rating_username, feedback_username, isbn13)
        cur.execute(query)
        if cur.rowcount == 0:
            return False
        else:
            return True

def rateFeedback(isbn13,rating_username,feedback_username,score):
    '''
    Returns True if user has given feedback for particular book.
    '''
    if userHasRateFeedback(isbn13,rating_username,feedback_username):
        return False

    else:
        con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
        with con:
            cur = con.cursor()
            now = datetime.datetime.now()
            query = "INSERT INTO rating VALUES " \
                    "('{0}','{1}',{2},'{3}',{4});".format(rating_username,feedback_username,isbn13,now.strftime("%Y-%m-%d"),score)
            cur.execute(query)

def getNFeedbacksForBook(isbn13,n,username):
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
        query = "SELECT * FROM feedback NATURAL JOIN ("\
                "SELECT feedback_user,isbn13,average,score AS rat_score FROM (SELECT * FROM " \
                "(SELECT feedback_user, isbn13, AVG(score) as average " \
                "FROM rating " \
                "GROUP BY feedback_user, isbn13) A " \
                "WHERE A.isbn13 = '{0}' " \
                "ORDER BY A.average DESC " \
                "LIMIT {1}) J "\
                "NATURAL LEFT JOIN "\
                "(SELECT * FROM rating "\
                "WHERE rating_user = '{2}' "\
                "AND isbn13 = '{0}') K) L " \
                "ORDER BY average DESC;".format(isbn13,n,username) #Limit selects top n rows for MYSQL. If SQL server use SELECT TOP n FROM
        cur.execute(query)
        if cur.rowcount == 0:
            return None
        else:
            row = cur.fetchall()
            return row