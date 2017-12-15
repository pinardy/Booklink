# 50.008 Database Project (2017): Booklink
Bookstore Database-system with Django 

<b>Group members:</b>
1) Pinardy Yang 
2) Joshua Lim
3) Jway Jin Jun 
4) Eiros Tan
5) Sanjay Pushparajan

<b>Instructions:</b>__
Ensure that you have setup the database with the following details:
- Database name: bookstore
- User: bookstore_user
- Password: password
- Host: 127.0.0.1
- Port: 3306

After setting up the database, perform the following steps:

- Run <b>schema.py</b> to create the tables. (schema.py contains the DDL)
- Run createSQL.py (Inserts dummy data into the database, so we can view some books in the bookstore)
- Run populate.py to populate the database.

Run the command 'python manage.py runserver' and go to <b>127.0.0.1:8000/booklist/browse</b> once you are done.

The links below show where our functions and other SQL codes are used

- schema.py: https://github.com/pinardy/DB-Project/blob/master/bookstore/schema.py
- book.py: https://github.com/pinardy/DB-Project/blob/master/bookstore/booklist/query/book.py
- cart.py: https://github.com/pinardy/DB-Project/blob/master/bookstore/booklist/query/cart.py
- feedback.py: https://github.com/pinardy/DB-Project/blob/master/bookstore/booklist/query/feedback.py
- user.py: https://github.com/pinardy/DB-Project/blob/master/bookstore/booklist/query/user.py
