from django.db import models

# Create your models here.

# Models disallowed for this project
"""
class Book(models.Model):
	title = models.CharField(max_length=100)
	PAPERBACK = 'PB'
	HARDCOVER = 'HC'
	COVER_CHOICES = (
		(PAPERBACK, 'paperback'),
		(HARDCOVER, 'hardcover')
	)
	cover_format = models.CharField(
		max_length=2,
		choices=COVER_CHOICES,
	)
	num_pages = models.PositiveIntegerField()
	authors = models.CharField(max_length=200, blank=True)
	publisher = models.CharField(max_length=200, blank=True)
	year_publish = models.DateField(null=True, blank=True)
	edition = models.PositiveIntegerField(null=True, blank=True)
	ISBN10 = models.CharField(max_length=10, unique=True)
	ISBN13 = models.CharField(max_length=13, primary_key=True)
	
	def __str__(self):
		return '%s - %s' % (self.title, self.authors)
	
class User(models.Model):
	login_name = models.CharField(max_length=20, unique=True)
	password = models.CharField(max_length=20)
	
	def __str__(self):
		return self.login_name

class PurchaseHistory(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	num_copies = models.PositiveIntegerField()
	order_date = models.DateField(null=True, blank=True)
	
	def __str__(self):
		return '%s has purchased %d copies of book %s' % (self.user, self.num_copies, self.book)

class Inventory(models.Model):
	book = models.OneToOneField(Book, on_delete=models.CASCADE, primary_key=True)
	num_copies = models.PositiveIntegerField()
	
	def __str__(self):
		return '%s - %d copies' % (self.book, self.num_copies)

class Feedback(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	score = models.PositiveIntegerField()
	feedback = models.CharField(max_length=1000, blank=True)
	order_date = models.DateField(null=True, blank=True)

class Rating (models.Model):
	rating_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating_user')
	feedback_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedback_user')
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	score=models.PositiveIntegerField()
	entry_date = models.DateField()
"""