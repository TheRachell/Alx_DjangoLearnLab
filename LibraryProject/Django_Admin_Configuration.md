# Django Admin Configuration for Book Model

## Objective
To integrate the Book model with the Django admin interface and enhance usability by customizing the admin display.

## Steps

1. Registered the Book model in `bookshelf/admin.py`:
   ```python
   from django.contrib import admin
   from .models import Book

   @admin.register(Book)
   class BookAdmin(admin.ModelAdmin):
       list_display = ('title', 'author', 'publication_year')
       search_fields = ('title', 'author')
       list_filter = ('publication_year',)

