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
   - since the databease is preconfigured and is provided into the repo the step can be skipped 
  

## Usage
1. Run the development server:
   - ``poetry run python manage.py runserver``
2. Accessing the API endpoints through the following URLs:
   - Users: [http://127.0.0.1:8000/api/users/](http://127.0.0.1:8000/api/users/)
   - Genres: [http://127.0.0.1:8000/api/genres/](http://127.0.0.1:8000/api/genres/)   
   - Books: [http://127.0.0.1:8000/api/books/](http://127.0.0.1:8000/api/books/)
   - Book Details: [http://127.0.0.1:8000/api/bookdetails/](http://127.0.0.1:8000/api/bookdetails/)
   - Get Borrowed Books details : [http://127.0.0.1:8000/api/borrowedbooks/](http://127.0.0.1:8000/api/borrowedbooks/)
   - Submit Borrowed Book: [http://127.0.0.1:8000/api/submitborrowedbook/](http://127.0.0.1:8000/api/submitborrowedbook/)
   - users by id : `http://127.0.0.1:8000/api/users/id/` **Example** : [http://127.0.0.1:8000/api/users/1/](http://127.0.0.1:8000/api/users/1/)
   - generes by id : `http://127.0.0.1:8000/api/genres/id/` **Example** : [http://127.0.0.1:8000/api/genres/1/](http://127.0.0.1:8000/api/genres/1/)
   - Booksdetail by id : `http://127.0.0.1:8000/api/bookdetails/id/` **Example** : [http://127.0.0.1:8000/api/bookdetails/1/](http://127.0.0.1:8000/api/bookdetails/1/)
   - Submit Borrowd Books : `http://127.0.0.1:8000/api/submitborrowedbook/borrowed_id/` **Example** : [http://127.0.0.1:8000/api/submitborrowedbook/4/](http://127.0.0.1:8000/api/submitborrowedbook/4/) construct a del request and delete data from database the user can be seened but the books borrowed section will be an empty list
  
3. **Alternetly** , one can use the admin site to make some changes into the enpoints
  - Admin : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
  - Email : `admin@test.com` ,  password : `admin`
---

#### **NOTE** : since for the auth both basci and jwt are used
- For **basic auth** **admin credintial** can be used or **one can create a user form admin pannel** and use it
- For **jwt**
  - **jwt token pair**  : [http://127.0.0.1:8000/api/token/](http://127.0.0.1:8000/api/token/)
  - **jwt acess token form refresh token** : [http://127.0.0.1:8000/api/token/refresh/](http://127.0.0.1:8000/api/token/refresh/)
  
