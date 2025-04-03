from django.db import models

# Create your models here.
class Author(models.Model):
    # This model represents an author. Each author can have multiple books.

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    # This model represents a book, which belongs to a single author.

    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title