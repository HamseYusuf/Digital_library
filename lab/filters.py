import django_filters

from.models import Book

import django_filters

class BookFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(lookup_expr='icontains')
    publication_date = django_filters.NumberFilter(field_name='publication_date', lookup_expr='year')
    
    class Meta:
        model = Book
        fields = ['author' , 'category', 'publication_date']