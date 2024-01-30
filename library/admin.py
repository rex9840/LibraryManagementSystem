from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(LibraryUser)
class CustomAdminUser(admin.ModelAdmin):
    list_display = ['id','email','username','is_active','membership_date','is_admin','is_staff']
    list_filter = ['id','email','username','is_active','membership_date','is_admin','is_staff']
    exclude = ['last_login']


@admin.register(Genre)
class CustomAdminGenre(admin.ModelAdmin):
    list_display = ['id','genre_name']
    include = '__all__'


@admin.register(Book)
class CustomAdminBook(admin.ModelAdmin):
    list_display = ['book_id','title','ISBN','published_date','display_genre']
    list_filter = ['title','ISBN','published_date','genre']
    include = '__all__'
    

    def display_genre(self,obj):
        return ', '.join([genre.genre_name for genre in obj.genre.all()])
    
    display_genre.short_description = 'Genre'

@admin.register(BookDetail)
class CustomAdminBookDetails(admin.ModelAdmin):
    list_display = ['details_id','book_id','number_of_pages','publisher','language']
    list_filter = ['book_id','number_of_pages','publisher','language']
    include = '__all__'


@admin.register(BorrowedBook)
class CustomAdminBorrowedBooks(admin.ModelAdmin):
    list_display = ['book_id','borrowed_date','return_date','display_user']
    list_filter = ['book_id','borrowed_date','return_date']
    include = '__all__'
    
    def display_user(self,obj):
        return obj.user_id.username
    display_user.short_description = 'User Name'


@admin.register(UserBorrowedBook)
class CustomAdminUser(admin.ModelAdmin):
    list_display = ['display_user','display_borrowed_books']
    list_filter = ['user_id']
    include = '__all__'
    
    def display_user(self,obj):
        return obj.user_id.username
    display_user.short_description = 'User Name'

    def display_borrowed_books(self,obj):
        return ', '.join([book.__str__() for book in obj.burrowed_books.all()])
    
    display_borrowed_books.short_description = 'Borrowed Books'
