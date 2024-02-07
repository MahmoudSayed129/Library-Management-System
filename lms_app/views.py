from contextlib import redirect_stderr
from turtle import title
from django.shortcuts import render, redirect
from .models import Book, Catagory
from .forms import *
# Create your views here.
def index(request):
    if request.method == 'POST':
        new_book = BookForm(request.POST, request.FILES)
        if new_book.is_valid():
            new_book.save()
        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()
    context = {
        'books' : Book.objects.all(),
        'categories' : Catagory.objects.all(),
        'bookform' : BookForm(),
        'catform' : CategoryForm(),
        'allbooks' : Book.objects.filter(active = True).count(),
        'booksavailable' : Book.objects.filter(status = 'available').count(),
        'bookssold' : Book.objects.filter(status = 'sold').count(),
        'booksrented' : Book.objects.filter(status = 'rented').count(),
    }
    return render(request, "pages/index.html", context)

def search(request):
    if request.method == 'POST':
        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()
      
    else:
        search = ""
        if request.GET['search_name']:
            search = request.GET['search_name']
        context = {
            'books' : Book.objects.filter(title = search),
            'categories' : Catagory.objects.all(),
            'catform' : CategoryForm(),
            'search' : search,
        }
        return render(request, "pages/books.html", context)

def update(request, id):
    book = Book.objects.get(id = id)
    if request.method == 'POST':
        new_book = BookForm(request.POST, request.FILES, instance=book)
        if new_book.is_valid():
            new_book.save()
        return redirect('/')
    else:
        new_book = BookForm(instance=book)
    context = {
        'form' : new_book,
    }
    return render(request, "pages/update.html", context)

def delete(request, id):
    book = Book.objects.get(id = id)
    if request.method == 'POST':
        book.delete()
        return redirect('/')
    return render(request, "pages/delete.html")
