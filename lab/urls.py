from django.urls import path
from .views import home , create_book , create_category , create_school , book_detail

urlpatterns = [
    path('',home , name='book-list'),
    path('create_category/', create_category, name='create_category'),
    path('create_book/', create_book, name='create_book'),
    path('create_school/', create_school, name='create_school'),
    path('book/<int:pk>/', book_detail, name='book_detail'),

]