from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from .models import Book
from .forms import CategoryForm, BookForm 
from .models import Category, Book
from.filters import  BookFilter
import random
import mimetypes

def home(request):
    # categories = Category.objects.all()
    # books = Book.objects.all()
    # random_books_by_category = {cat:random.choice(books.filter(category = cat)) for cat in categories}

    # context = {
    #     "books": Book.objects.all()
    # }

    books = Book.objects.all()
    
    context = {
        'books': books,
    }

    return render(request, 'lab/home.html', context)

def download_book(request, book):
    try:
        book = get_object_or_404(Book, id=book)
        path = book.src_pdf.path
        file = open(path, 'r')
        filename = f"{book.title.replace(' ', '_')}.{book.src_file_type()}"
        response = HttpResponse(file, content=mimetypes.guess_type(filename))
        response['Content-Disposition'] = f"attachment; filename={filename}"
        return response    
    except:
        return render(request, "lab/404.html")
    

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = CategoryForm()

    return render(request, 'lab/create_category.html', {'form': form})

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'lab/create_book.html', {'form': form})
       

# def home(request):
#     book_filter = BookFilter(request.GET, queryset=Book.objects.all())
#     books = book_filter.qs
#     logo = Logo.objects.all()
#     context = {
#         'books': books,
#         'logo': logo,
#         'book_filter': book_filter,
#     }
#     return render(request, 'lab/list.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {
        'book': book
    }
    return render(request, 'lab/book_detail.html', context)