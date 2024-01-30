from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(LibraryUser)
class CustomAdminUser(admin.ModelAdmin):
    list_display = ['id','email','username','is_active','membership_date','is_admin','is_staff']
    list_filter = ['id','email','username','is_active','membership_date','is_admin','is_staff']
    exclude = ['last_login']


@admin.register(GenreModel)
class CustomAdminGenre(admin.ModelAdmin):
    include = '__all__'


@admin.register(BookModel)
class CustomAdminBook(admin.ModelAdmin):
    include = '__all__'


@admin.register(BookDetailsModel)
class CustomAdminBookDetails(admin.ModelAdmin):
    include = '__all__'


@admin.register(BorrowedBooks)
class CustomAdminBorrowedBooks(admin.ModelAdmin):
    include = '__all__'


