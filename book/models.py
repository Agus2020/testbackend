from django.db import models


class Library(models.Model):

    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Book(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey('book.Author', on_delete=models.CASCADE)
    libraries = models.ManyToManyField('book.Library')
    def __str__(self):
        return self.title


class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name

class Leads(models.Model):
    Email = models.EmailField(max_length=100)
    Fullname = models.CharField(max_length=40)
    Phone = models.DecimalField(max_digits=10,decimal_places=1)
    Library = models.ForeignKey(Library, on_delete=models.CASCADE)
   