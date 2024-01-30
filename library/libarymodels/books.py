from django.db import models
from  django.conf import settings



class Genre(models.Model):
    genre_name = models.CharField(max_length=100, db_column='GenreName')
    
    def __str__(self):
        return self.genre_name


class Book(models.Model):
    book_id = models.AutoField(primary_key=True, db_column='BookID')
    title = models.CharField(max_length=100, db_column='Title')
    ISBN  = models.CharField(max_length=100, db_column='ISBN')
    published_date= models.DateField(db_column='PublishedDate')
    genre = models.ManyToManyField(Genre, db_column='Genre')

    class Meta:
        ordering = ['book_id']

    def __str__(self):
        return self.title



class BookDetail(models.Model): 
    details_id = models.AutoField(primary_key=True, db_column='DetailsID')
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE, db_column='BookID')
    number_of_pages = models.IntegerField(db_column='NumberOfPages')
    publisher = models.CharField(max_length=100, db_column='Publisher')
    language = models.CharField(max_length=100, db_column='Language')
    
    class Meta:
       ordering = ['book_id']

    def __str__(self):
        return self.book_id.title

class BorrowedBook(models.Model): 
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.RESTRICT, db_column='UserID')
    borrowed_id = models.AutoField(primary_key=True, db_column='BorrowedID')
    book_id = models.ForeignKey(Book,on_delete=models.RESTRICT, db_column='BookID')
    borrowed_date = models.DateField(db_column='BurrowedDate')
    return_date = models.DateField(db_column='ReturnDate')
    class Meta:
        ordering = ['borrowed_date']

    def __str__(self):
        return self.book_id.title

