from django import forms
from .models import Category, Book

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class RegisterForm(forms.Form):
    username = forms.CharField(strip=True)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())