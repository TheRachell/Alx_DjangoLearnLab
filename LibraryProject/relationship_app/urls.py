from django.urls import path 
from .views import list_books, LibraryDetailView, register_view, login_view, logout_view
from .views import admin_view, librarian_view, member_view
from . import views 

urlpatterns = [
    path('books/', list_books, name = 'list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name= 'library_detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('add', views.add_book, name='add_book'),
    path('edit/<int:book_id>', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book')
]