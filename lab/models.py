from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.department_name

class Category(models.Model):
    category_name = models.CharField(max_length=50, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=50, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.subcategory_name

class Book(models.Model):
    author = models.CharField(max_length=50, null=True)
    book_title = models.CharField(max_length=200, null=True)
    summary = models.CharField(max_length=200 , null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    publication_date = models.DateField(null=True)
    cover_image = models.ImageField(upload_to='book_covers', max_length=200, blank=True, null=True)
    pdf_book = models.FileField(upload_to='pdf_books', max_length=200, blank=True, null=True)



class Video(models.Model):
    title = models.CharField(max_length=200)
    Video = models.FileField(upload_to='videos')

    def __str__(self):
        return self.title



class School(models.Model):
    school_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.school_name

class Logo(models.Model):
    atu_logo = models.ImageField(upload_to='atu_logo', blank=True, null=True)
