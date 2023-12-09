from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name
    


class Book(models.Model):
    author = models.CharField(max_length=50, null=False)
    title = models.CharField(max_length=200, null=False)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    summary = models.TextField(blank=True)
    published_at = models.DateField()
    cover = models.ImageField(upload_to='book_covers', max_length=200, blank=True)
    src_pdf = models.FileField(upload_to='pdf_books', max_length=200, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.author} - {self.title}"
    
    def src_file_type(self):
        filename = self.src_pdf.name.split(".")
        return filename[-1]

class Collection(models.Model):
    owner = models.OneToOneField(User, blank=True, on_delete=models.CASCADE)
    books  = models.ManyToManyField(Book, related_name="collections", blank=True)

    def __str__(self):
        return f"{self.owner.username}'s collection"