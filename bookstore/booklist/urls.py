from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^base/$', views.base, name='base'),
    url(r'^work/$', views.work, name='work'),
    url(r'^login/$', views.login, name='login'),
    url(r'^testview/$', views.testview, name='testview'),
]