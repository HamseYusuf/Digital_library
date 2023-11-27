from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from .models import Book
from .forms import CategoryForm, BookForm , SchoolForm
from .models import Category, Book , School , Logo
from.filters import  BookFilter

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = CategoryForm()

    return render(request, 'lab/create_category.html', {'form': form})


def create_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = SchoolForm()

    return render(request, 'lab/create_school.html', {'form': form})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'lab/create_book.html', {'form': form})
       

def home(request):
    book_filter = BookFilter(request.GET, queryset=Book.objects.all())
    books = book_filter.qs
    logo = Logo.objects.all()
    context = {
        'books': books,
        'logo': logo,
        'book_filter': book_filter,
    }
    return render(request, 'lab/list.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {
        'book': book
    }
    return render(request, 'lab/book_detail.html', context)