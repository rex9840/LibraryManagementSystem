from django.db import models
from django.conf import settings
from .books import BorrowedBook


class UserBorrowedBook(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, db_column='UserID')
    burrowed_books = models.ManyToManyField(BorrowedBook,db_column='BorrowedBooks')
