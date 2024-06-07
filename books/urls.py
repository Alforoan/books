from django.contrib import admin
from django.urls import path, include
from .views import show_books

urlpatterns = [
    path('books/', show_books, name='show_books')
]
