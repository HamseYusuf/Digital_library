from django.shortcuts import render , redirect , get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView
from django.http import FileResponse
from .models import Book
from django.contrib.auth.models import User
from .forms import CategoryForm, BookForm, RegisterForm
from .models import Category, Book
from.filters import  BookFilter
import mimetypes

@login_required()
def home(request):
    books = Book.objects.all()
    
    context = {
        'books': books,
    }

    return render(request, 'lab/home.html', context)


@login_required()
def download_book(request, book):
    book = get_object_or_404(Book, id=book)
    path = book.file.path
    file = open(path, 'rb')
    response = FileResponse(file, as_attachment=True)
    return response
    

@login_required()
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = CategoryForm()

    return render(request, 'lab/create_category.html', {'form': form})


@login_required()
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'lab/create_book.html', {'form': form})
       

class Login(LoginView):
    template_name = "lab/login.html"
    next_page = "home"


class Register(FormView):
    template_name = "lab/register.html"
    form_class = RegisterForm

    def get_success_url(self) -> str:
        return reverse("home")

    def form_valid(self, form: RegisterForm):
        user = User.objects.create_user(form.data['username'], form.data['email'], form.data['password'])
        return super().form_valid(form)
    
    


class Logout(LogoutView):
    template_name = ""


def search(request):
    q = request.GET.get("q")
    books = Book.objects.filter(title__contains=q)
    context = {
        "books": books,
        "q": q
    }

    return render(request, "lab/search.html", context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {
        'book': book
    }
    return render(request, 'lab/book_detail.html', context)