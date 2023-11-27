from django.contrib import admin
from .models import Category, Book, School , Logo

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(School)
admin.site.register(Logo)