# Advanced API Project

## Overview
This Django REST Framework (DRF) project implements a REST API for managing books and authors. It includes CRUD operations using generic views.

## Features
- **List books** (`GET /api/books/`)
- **Retrieve book details** (`GET /api/books/<id>/`)
- **Create a new book** (`POST /api/books/create/`) *(Authenticated users only)*
- **Update a book** (`PUT /api/books/<id>/update/`) *(Authenticated users only)*
- **Delete a book** (`DELETE /api/books/<id>/delete/`) *(Authenticated users only)*

## Installation
```bash
git clone https://github.com/YOUR_USERNAME/Alx_DjangoLearnLab.git
cd advanced-api-project
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## 🔎 API Filtering, Searching, and Ordering

### Filtering:
You can filter books using:
- `?title=Book Title`
- `?author=<author_id>`
- `?publication_year=2023`

### Searching:
Use `?search=` to perform a full-text search across:
- Book title
- Author name

Example:

### Ordering:
Use `?ordering=` with any sortable field:
- `?ordering=title`
- `?ordering=-publication_year`

Prefix with `-` to sort in descending order.
