# Library Management System

## Overview
This is a Library Management System built with Django as the backend API service and SQLite as the default database. The system allows users to manage books, genres, users, borrowed books, and submitted books.


## Prerequisites
- Python 3.x
- Poetry

## Installation

1. Clone the repository:
2. Install dependencies:
   -  ``poetry install``
3. Set up the database:
   - ``poetry run python manage.py migrate``
  

## Usage
1. Run the development server:
   - ``poetry run python manage.py runserver``
2. Accessing the API endpoints through the following URLs:
- User: [http://127.0.0.1:8000/api/user/](http://127.0.0.1:8000/api/user/)
- Genre: [http://127.0.0.1:8000/api/genre/](http://127.0.0.1:8000/api/genre/)
- Book: [http://127.0.0.1:8000/api/book/](http://127.0.0.1:8000/api/book/)
- Book Details: [http://127.0.0.1:8000/api/bookdetails/](http://127.0.0.1:8000/api/bookdetails/)
- Borrowed Books: [http://127.0.0.1:8000/api/borrowedbooks/](http://127.0.0.1:8000/api/borrowedbooks/)
- Submit Book: [http://127.0.0.1:8000/api/submitbook/](http://127.0.0.1:8000/api/submitbook/)
3. **Alternetly** , one can use the admin site to make some changes into the enpoints
  - Admin : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
  - Email : `admin@test.com` ,  password : `admin`
  
