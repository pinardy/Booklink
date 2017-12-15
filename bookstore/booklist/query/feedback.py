import MySQLdb as mdb
import datetime

def userHasGivenFeedback(isbn13,username):
    '''
    :param isbn13: isbn13 of the book
    :param username: name of the user
    :return: True if user has given feedback for particular book.
    '''
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
        query = "SELECT * " \
                "FROM feedback " \
                "WHERE feedback_user = '{0}' and isbn13 = '{1}';".format(username, isbn13)
        cur.execute(query)
        if cur.rowcount == 0:
            return None
        else:
            row = cur.fetchall()
            return row

def writeFeedback(isbn13,username,score,text):
    '''
    :param isbn13: isbn13 of the book
    :param username: name of the user
    :param score: score that the user will give
    :param text: the string of the feedback to be given
    :return: True if user has given feedback for particular book
    '''

    if userHasGivenFeedback(isbn13, username) is not None:
        return False

    else:
        con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
        with con:
            cur = con.cursor()
            now = datetime.datetime.now()
            query = "INSERT INTO feedback VALUES " \
                    "('{0}','{1}','{2}','{3}','{4}');".format(username, isbn13, now.strftime("%Y-%m-%d"), score, text)
            cur.execute(query)
        rateFeedback(isbn13, 'admin', username, 0) #Initialize an admin rating of 0, so it can appear in testimonial

def userHasRateFeedback(isbn13,rating_username,feedback_username):
    '''
    :param isbn13: isbn13 of the book
    :param rating_username:  currently logged in person giving the rating
    :param feedback_username: name of the person that is being rated
    :return: True if user has given feedback for particular book
    '''
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
        query = "SELECT * " \
                "FROM rating " \
                "WHERE rating_user = '{0}' and feedback_user = '{1}' and isbn13 = '{2}';".format(rating_username, feedback_username, isbn13)
        cur.execute(query)
        if cur.rowcount == 0:
            return False
        else:
            return True

def rateFeedback(isbn13,rating_username,feedback_username,score):
    '''
    :param isbn13: isbn13 of the book
    :param rating_username: currently logged in person giving the rating
    :param feedback_username: name of the person that is being rated
    :param score: score to be assigned to a feedback rating
    :return: True if user has given feedback for particular book
    '''
    if userHasRateFeedback(isbn13,rating_username,feedback_username):
        return False

    else:
        con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
        with con:
            cur = con.cursor()
            now = datetime.datetime.now()
            query = "INSERT INTO rating VALUES " \
                    "('{0}','{1}','{2}','{3}',{4});".format(rating_username,feedback_username,isbn13,now.strftime("%Y-%m-%d"),score)
            cur.execute(query)

def getNFeedbacksForBook(isbn13,n,username):
    '''
    :param isbn13: book that specifies which feedbacks to view
    :param n: max number of feedback to view
    :param username: logged in user
    :return: Nested tuple of the top n feedbacks for a particular book, or None if there is none.
    Query: Innermost sub-query aggregates all ratings given for each (user's feedback,book) tuple.
    Next innermost sub-query selects all ratings of the requested book isbn13 and ranks them in order, finally imposing max number of feedbacks to view.
    '''
    con = mdb.connect(host="127.0.0.1", port=3306, user="bookstore_user", passwd="password", db="bookstore")
    with con:
        cur = con.cursor()
        query = "SELECT * FROM feedback NATURAL JOIN ( "\
                    "SELECT feedback_user,isbn13,average,score AS rat_score FROM ( " \
                        "SELECT * FROM ( " \
                        "SELECT feedback_user, isbn13, AVG(score) as average " \
                        "FROM rating " \
                        "GROUP BY feedback_user, isbn13) A " \
                    "WHERE A.isbn13 = '{0}' " \
                    "ORDER BY A.average DESC " \
                    "LIMIT {1}) J "\
                "NATURAL LEFT JOIN ( "\
                    "SELECT * FROM rating "\
                    "WHERE rating_user = '{2}' "\
                    "AND isbn13 = '{0}') K) L; ".format(isbn13,n,username) #Limit selects top n rows for MYSQL. If SQL server use SELECT TOP n FROM
        cur.execute(query)
        if cur.rowcount == 0:
            return None
        else:
            row = cur.fetchall()
            return row