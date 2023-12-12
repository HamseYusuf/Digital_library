from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('',views.home , name='home'),
    path('create_category/', views.create_category, name='create_category'),
    path('create_book/', views.create_book, name='create_book'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/download/<int:book>/', views.download_book, name='download_book'),
    path('search', views.search, name='search'),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]