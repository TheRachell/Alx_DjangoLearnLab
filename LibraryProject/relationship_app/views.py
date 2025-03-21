from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Book, Library
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
# Create your views here.
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
    

