## 🔐 User Authentication System

This Django blog project features a full user authentication system to allow users to register, log in, log out, and manage their profiles securely.

---

### ✨ Features

- User registration with username, email, and password
- User login and logout using Django's built-in views
- Profile page viewable only to logged-in users
- CSRF protection on all forms
- Secure password hashing with Django’s authentication system

---

### 🛠️ Setup Instructions

1. **Ensure Django is installed:**

```bash
pip install django


## 📝 Blog Post Management (CRUD)

This feature enables full blog post management with Create, Read, Update, and Delete operations for blog content. Built using Django’s class-based views, it allows users to manage their own posts while providing readers with access to all blog content.

---

### ✨ Features

- 📃 View all blog posts
- 🔍 View detailed content for individual posts
- ✍️ Create new blog posts (authenticated users only)
- 🛠️ Update existing posts (only by author)
- ❌ Delete posts (only by author)

---

### 🛠️ Setup Instructions

1. **Post Model (in `models.py`):**

```python
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
