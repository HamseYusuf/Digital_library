from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Book(models.Model):
    author = models.CharField(max_length=50, null=False)
    book_title = models.CharField(max_length=200, null=False)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='book_covers', max_length=200, blank=True)
    pdf_book = models.FileField(upload_to='pdf_books', max_length=200, blank=True)

    def __str__(self):
        return self.author

class School(models.Model):
    school_name = models.CharField(max_length=50)

    def __str__(self):
        return self.school_name

class Logo(models.Model):
    atu_logo = models.ImageField(upload_to='atu_logo', blank=True)
