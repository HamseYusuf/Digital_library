from django import forms
from .models import Category, Book , School  , SubCategory

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


class BookSearchForm(forms.Form):
    author = forms.CharField(required=False)
    book_title = forms.CharField(required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    subcategory = forms.ModelChoiceField(queryset=SubCategory.objects.all(), required=False)
