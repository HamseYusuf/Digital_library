from django.urls import path
from .views import list , book_detail , home , custom_login, signup, custom_logout , video

urlpatterns = [
    path('', home , name="home"), 
    path('logout/', custom_logout, name='logout'),
    path('list/',list , name='book-list'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('login/', custom_login, name='login'),
    path('signup/', signup, name='signup'),
    path('video/' , video , name='videos')

]