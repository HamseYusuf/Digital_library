from django.urls import path
from .views import home , create_book , create_category  , book_detail, download_book

urlpatterns = [
    path('',home , name='book-list'),
    path('create_category/', create_category, name='create_category'),
    path('create_book/', create_book, name='create_book'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('book/download/<int:book>/', download_book, name='download_book')
]