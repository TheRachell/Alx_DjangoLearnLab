from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Book, Library
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.http import HttpResponse


def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    models = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def check_role(role):
    def decorator(user):
        return user.is_authenticated and user.userprofile.role == role
    return decorator 

@user_passes_test(check_role('Admin'))
def admin_view(request):
    return HttpResponse("Welcome to the Admin page!")

@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return HttpResponse("Welcome to the Librarian page!")

@user_passes_test(check_role('Member'))
def member_view(request):
    return HttpResponse("Welcome to the Member page!")  

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        Book.objects.create(title=title, author=author, published_date=published_date)
        return redirect('book_list')
    return render(request, 'add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method =='POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.published_date = request.POST.get('published_date')
        book.save()
        return redirect('book_list')
    return render(request, 'edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('book_list')
    

