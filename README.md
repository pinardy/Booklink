# 50.008 Database Project (2017): Booklink
Bookstore Database-system with Django 

<b>Group members:</b>
1) Pinardy Yang (1001520)
2) Joshua Lim (1001509)
3) Jway Jin Jun (1001555)
4) Eiros Tan ()
5) Sanjay Pushparajan (1001646)

<b>Instructions:</b>
 Ensure that you have setup the database with the following details:
- Database name: bookstore
- User: bookstore_user
- Password: password
- Host: 127.0.0.1
- Port: 3306

After setting up the database, perform the following steps:

- Run <b>schema.py</b> to create the tables. (schema.py contains the DDL)
- Run <b>createSQL.py</b> (Inserts dummy data into the database, so we can view some books in the bookstore)
- Run <b>populate.py</b> to populate the database.
-> If any error occurs during the execution of <b>populate.py</b>, it is due to certain characters in the book title and is normal. The script still works so long as some data is populated into the database.
- Create a superuser with the command 'python manage.py createsuperuser'. This superuser account will act as the bookstore manager account which will allow us to do commands specific to staff accounts. Name the superuser account as 'admin'

Run the command 'python manage.py runserver' and go to <b>127.0.0.1:8000/booklist/browse</b> once you are done.

The links below show where our functions and other SQL codes are used

- schema.py: https://github.com/pinardy/DB-Project/blob/master/bookstore/schema.py
- book.py: https://github.com/pinardy/DB-Project/blob/master/bookstore/booklist/query/book.py
- cart.py: https://github.com/pinardy/DB-Project/blob/master/bookstore/booklist/query/cart.py
- feedback.py: https://github.com/pinardy/DB-Project/blob/master/bookstore/booklist/query/feedback.py
- user.py: https://github.com/pinardy/DB-Project/blob/master/bookstore/booklist/query/user.py

<b>Git-tracked development workflow</b>
In our project, we make use of GitHub version control for our project to enable us to manage our project in an organised, less-risky manner.

Thanks to GitHub, each of the group member can work on individual parts remotely without having fear of overriding each other’s work unnecessarily. In the case where a part has merge conflicts, the group can decide what to keep and what to remove. With the use of branches and merging, the group can efficiently work on the project as each member will not have to worry about messing up the project if multiple people are working on the same part. 

Assume that multiple people are working on the project, possibly making edits to the same file. How do we know the members’ work will not be unnecessarily overwritten? Assume each member is working on their part on their own branch. Listed below is a typical workflow for a team member for safe merging.


On branch:
  - git add <changes to files>           (Add changes and prepare for commit)
  - git commit -m "your message"    (Informing others what changed)
  - git push origin                              (Push the changes onto branch)
  - git checkout master                     (Change branch to master branch)

MASTER:
  - git pull                                          (Get latest changes if any)
  - git checkout <branch>                 (Change branch to personal branch)

BRANCH:
  - git merge <master>                     (Merge branch with master)
>> at this point, there could be conflicts in the code, which you will need to resolve <<
  - git commit -m 'message'              (Informing others what changed)
  - git push                                        (Push the changes onto branch)
  - git checkout master                     (Change branch to master branch)


MASTER:
  - git merge <branch>                   (Merge master with personal branch)
  - git push                                     (Push the changes onto master)
  
  
<b>jQuery</b>
jQuery is a cross-platform JavaScript library designed to simplify the client-side scripting of HTML. In our project, we make use of AJAX (Asynchronous JavaScript and XML) to make the process of ordering books a smooth and seamless process.

Through the use of jQuery we learnt three aspects of it:
Concept and implementation of AJAX requests
In page scripting to fetch and update HTML elements
Adding interactivity to our application

The AJAX requests asynchronously performed GET and POST operations to a given view tied to a function at the /ajax/XXXXX endpoint. The response is a HTTP response code (for a POST request) and a returned row (for a GET request) for updating parts of the Django page template without triggering a page refresh. This allows for multiple functions to coexist on the same page without the need for a very fragmented app.

JQuery was also used for elements of interaction- eg. modals and tool tips. Calling scripts in a webpage allowed us to access specific HTML elements (identified by their name) and whose value was tied to their ISBN13 credentials. This allowed effects such as popups and information shown on hovering to be dynamically displayed (as seen in the browse page).


