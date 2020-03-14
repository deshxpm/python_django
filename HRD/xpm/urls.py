# from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
	# path('', views.home, name='home'),
	path('', views.home, name = 'home'),
	path('registration/', views.registration, name='registration'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('websitehome/', views.websitehome, name='websitehome'),
]