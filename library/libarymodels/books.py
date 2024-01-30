from django.db import models



class GenreModel(models.Model):
    GenreName = models.CharField(max_length=100) 

class BookModel(models.Model):
    BookID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=100)
    PublishedDate = models.DateField()
    Genre = models.ManyToManyField(GenreModel)

    class Meta:
        ordering = ['BookID']


class BookDetailsModel(models.Model): 
    DetailsID = models.AutoField(primary_key=True)
    BookID = models.ForeignKey(BookModel,on_delete=models.CASCADE)
    NumberOfPages = models.IntegerField()
    Publisher = models.CharField(max_length=100)
    Language = models.CharField(max_length=100)
    
    class Meta:
       ordering = ['BookID']






class BorrowedBooks(models.Model): 
    BookID = models.ForeignKey(BookModel,on_delete=models.CASCADE)
    BurrowedDate = models.DateField()
    ReturnDate = models.DateField()

    class Meta:
        ordering = ['BurrowedDate']

