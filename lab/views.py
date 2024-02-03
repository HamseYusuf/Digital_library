from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout

def custom_logout(request):
    logout(request)
    return redirect('home')  

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Book, Logo
from .forms import BookSearchForm


def home(request):
    return render(request, 'lab/home.html')

@login_required
def list(request):
    form = BookSearchForm(request.GET)
    books = Book.objects.all()

    if form.is_valid():
        author = form.cleaned_data.get('author')
        book_title = form.cleaned_data.get('book_title')
        category = form.cleaned_data.get('category')
        subcategory = form.cleaned_data.get('subcategory')

        if author:
            books = books.filter(author__icontains=author)
        if book_title:
            books = books.filter(book_title__icontains=book_title)
        if category:
            books = books.filter(category=category)
        if subcategory:
            books = books.filter(subcategory=subcategory)

    logo = Logo.objects.all()
    context = {
        'books': books,
        'logo': logo,
        'form': form,
    }
    return render(request, 'lab/list.html', context)

@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    similar_books = Book.objects.filter(subcategory=book.subcategory).exclude(pk=pk)
    context = {
        'book': book,
        'similar_books': similar_books,
    }
    return render(request, 'lab/book_detail.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'lab/signup.html', {'form': form})

def custom_login(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password.'
    return render(request, 'lab/login.html', {'error_message': error_message})
