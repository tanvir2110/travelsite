# dappx/urls.py
from django.conf.urls import url
from dappx import views
from django.contrib import admin
from django.urls import path
from django.urls import include
# SET THE NAMESPACE!
app_name = 'dappx'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),

	#path('',views.head),
	path('user_login/delhi.html',views.delhi),
	path('user_login/about.html',views.about),
	path('user_login/destination.html',views.dest),
	path('user_login/agra.html',views.agra),
	path('user_login/delhi.html',views.delhi),
	path('user_login/h_page.html',views.head),
	path('user_login/header.html',views.header),
	path('user_login/jaipur.html',views.jaipur),
	path('user_login/hpme.html',views.home),
	path('user_login/kerala.html',views.kerala),
	path('user_login/kolkata.html',views.kolkata),
	path('user_login/map_page.html',views.map),
	path('user_login/varanasi.html',views.varanasi),
	path('user_login/login.html',views.user_logout),
	
	
	
	
]