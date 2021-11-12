'''
URLs for shorterner app urlshortener/urls.py
'''
from django.urls import path
from .views import home_view

appname = "shorterner"

urlpatterns = [

	path("",home_view, name = "home")
]