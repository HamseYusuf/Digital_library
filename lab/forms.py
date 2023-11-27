from django import forms
from .models import Category, Book , School

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['school_name']