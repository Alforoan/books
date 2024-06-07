from django.shortcuts import render, HttpResponse
from .models import Book

# Create your views here.
def show_books(request):
  books = Book.objects.all()
  context = {
    'books' : books
  }
  return render(request, 'books/books.html', context)
  