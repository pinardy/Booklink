from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from booklist.query.user import *
from booklist.query.admin import *
from booklist.query.cart import *
from booklist.query.feedback import *
from booklist.query.book import getAllBooks, searchBookByTitle, getBook

from booklist.forms import BookForm, StockForm, RegistrationForm

from booklist.helperFunctions import input_formatting

def index(request):
	return render(request, 'booklist/index.html', {})

def error(request):
	return render(request, 'booklist/error.html', {})

def browse(request):
	book_list = getAllBooks()
	context = {
		'book_list': book_list,
	}
	print (book_list)
	return render(request, 'booklist/browse.html', context)


def search(request):
	if request.method == 'GET':
		q =request.GET
		title = q.__getitem__('title')
		book_list = searchBookByTitle(title)
		context = {
			'book_list': book_list,
		}
		print (book_list)
		return render(request, 'booklist/browse.html', context)


def stock(request):
	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data.get('title')
			covFormat = form.cleaned_data.get('covFormat')
			noPages = form.cleaned_data.get('noPages')
			authors = form.cleaned_data.get('authors')
			publisher = form.cleaned_data.get('publisher')
			yearPublish = form.cleaned_data.get('yearPublish')
			edition = form.cleaned_data.get('edition')
			isbn10 = form.cleaned_data.get('isbn10')
			isbn13 = form.cleaned_data.get('isbn13')
			initStock = form.cleaned_data.get('quantity')
			# put update function here
			insertBook (title,covFormat,noPages,authors,publisher,yearPublish,edition,isbn10,isbn13, initStock)
	else:
		form = BookForm
	return render(request, 'booklist/stock.html', {'bookForm': form})


def register(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			form = RegistrationForm(request.POST)
			if form.is_valid():
				user = form.save()
				user.refresh_from_db()  # load the profile instance created by the signal
				user.save()
				username = form.cleaned_data.get('username')
				raw_password = form.cleaned_data.get('password1')
				user = authenticate(username=username, password=raw_password)
				login(request, user)
				# TODO: This should redirect to a success page
				return redirect('index')

		# If GET request
		else:
			form = RegistrationForm()
		return render(request, 'booklist/register.html', {'form': form})


def logout_view(request):
	logout(request)
	return render(request, 'booklist/index.html', {})


def login_view(request):
	"""
	Displays the login form and handles the login action.
	"""
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == "POST":
			form = AuthenticationForm(request, data=request.POST)
			if form.is_valid():

				username = form.cleaned_data.get('username')
				raw_password = form.cleaned_data.get('password')
				user = authenticate(username=username, password=raw_password)
				login(request, user)

				return redirect('index')
		else:
			form = AuthenticationForm()

		return render(request, 'booklist/login.html', {'form': form})


def profile(request):
	"""
	Profile Query
	"""
	if not (request.user.is_authenticated):
		return redirect('index')
	else:
		user_profile = retrieveProfile(request.user.username)
		purchase_history = getPurchaseHistory(request.user.username)
		feedback_history = getFeedbackHistory(request.user.username)

		rating_history = getRatingHistory(request.user.username)
		print(rating_history)
		return render(request, 'booklist/profile.html', {'user_profile': user_profile, 'purchase_history': purchase_history, 'feedback_history': feedback_history, 'rating_history': rating_history})


def staff_view(request):
	"""
	Staff page. Store managers can insert a new book or increase stock
	"""
	if not (request.user.is_authenticated):
		return redirect('login')
	elif not (request.user.is_superuser):
		return redirect('error')
	else:
		return render(request, 'booklist/staff.html', {})


def addbook(request):
	"""
	Staff page. Store managers can insert a new book or increase stock
	"""
	if not request.user.is_authenticated:
		return redirect('login')
	elif not request.user.is_superuser:
		return redirect('error')
	else:
		if request.method == 'POST':
			form = BookForm(request.POST)
			if form.is_valid():
				title = form.cleaned_data.get('title')
				covFormat = form.cleaned_data.get('covFormat')
				noPages = form.cleaned_data.get('noPages')
				authors = form.cleaned_data.get('authors')
				publisher = form.cleaned_data.get('publisher')
				yearPublish = form.cleaned_data.get('yearPublish')
				edition = form.cleaned_data.get('edition')
				isbn10 = form.cleaned_data.get('isbn10')
				isbn13 = form.cleaned_data.get('isbn13')
				quantity = form.cleaned_data.get('quantity')
				# put update function here
				insertBook(title, covFormat, noPages, authors, publisher, yearPublish, edition, isbn10, isbn13, quantity)
				return redirect('staff')
		else:
			form = BookForm
			return render(request, 'booklist/staff/addbook.html', {'form': form})


def addstock(request):
	"""
	Staff page. Store managers can insert a new book or increase stock
	"""
	if not request.user.is_authenticated:
		return redirect('login')
	elif not request.user.is_superuser:
		return redirect('error')
	else:
		if request.method == 'POST':
			form = StockForm(request.POST)
			if form.is_valid():
				isbn13 = form.cleaned_data.get('title')
				print(isbn13)
				quantity = form.cleaned_data.get('quantity')
				# put update function here
				updateInventory(isbn13, quantity)
				return redirect('staff')
		else:
			form = StockForm
			return render(request, 'booklist/staff/addstock.html', {'form': form})


def cart(request):
 """
 Staff page. Store managers can insert a new book or increase stock
 """
 if not request.user.is_authenticated:
  return redirect('login')
 else:
  if request.method == 'POST':
   req = request.POST
   if req.get('update'):
    modifyCart(req.get('isbn13'), request.user.username, req.get('quantity'))
   elif req.get('delete'):
    delFromCart(req.get('isbn13'), request.user.username)
   elif req.get('placeorder'):
    # isValid is None if there are no problematic purchases
    # isValid is a list if there are problematic purchases

    isValid = ValidPurchase(request.user.username)
    print(isValid)
    if isValid is None:
     PurchaseBook(request.user.username)
     delAllFromCart(request.user.username)
     return redirect('orderfinish')
    else:
     print("DEBUG: ONE OF YOUR ORDERS HAS EXCEEDED INVENTORY")
     return redirect('error')

   return redirect('cart')
  else:
   cart = showCart(request.user.username)
   if cart is None:
    return render(request, 'booklist/cart.html',{'cart':None})
   else:
    return render(request, 'booklist/cart.html',{'cart':cart})

def book(request,isbn13):
	no_feedback = 5
	if not request.user.is_authenticated:
		return redirect('login')
	else:

		if request.method == 'POST':
			req = request.POST
			if req.get('submit_feedback'):
				writeFeedback(isbn13, request.user.username, req.get('feedback_score'), req.get('feedback_text'))
			elif req.get('reselect_feedback'):
				no_feedback = req.get('no_views')
			elif req.get('submit_rating'):
				rateFeedback(isbn13, request.user.username, req.get("feedback_username"), req.get('rating_score'))


		given_feedback = userHasGivenFeedback(isbn13, request.user.username)
		feedback_ratings = getNFeedbacksForBook(isbn13, no_feedback, request.user.username)
		book_title = getBook(isbn13)
		return render(request, 'booklist/book.html', {'given_feedback': given_feedback,
													'book_title': book_title,
													'no_feedback': no_feedback,
													'feedback_ratings': feedback_ratings,
													'username': request.user.username})


def orderfinish(request):
	"""
	Thank you page
	"""
	return render(request, 'booklist/orderfinish.html', {})


def error(request):
	"""
	Error page
	"""
	return render(request, 'booklist/error.html', {})


def feedback(request):
	if request.method == "GET":
		q = request.GET
		isbn13 = q.__getitem__('isbn')

		book_details = getBook(isbn13)
		context = {
			'book_details': book_details,
		}
		print(book_details)
		#TODO: Replace the link with the appropriate one
		return render(request, 'booklist/feedback.html', context)