from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^browse/$', views.browse, name='browse'),
    url(r'^(?P<isbn13>[X0-9]+)/$', views.book, name='book'),
    url(r'^search/$', views.search, name='search'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^orderfinish/$', views.orderfinish, name='orderfinish'),
    url(r'^staff/$', views.staff_view, name='staff'),
    url(r'^staff/addstock/$', views.addstock, name='addstock'),
    url(r'^staff/addbook/$', views.addbook, name='addbook'),
    url(r'^staff/statistics/$', views.statistics, name='statistics'),
    url(r'^error/$', views.error, name='error'),
    url(r'^ajax/addBookToCart/$', views.addBooktoCart, name='addBooktoCart')
]

