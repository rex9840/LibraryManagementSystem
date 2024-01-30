from rest_framework import serializers
from .models import LibraryUser,GenreModel,BookModel,BookDetailsModel,BorrowedBooks

class LibraryUserSerialiser(serializers.Serializer): 
   class Meta:
      model = LibraryUser
      fields = ['id', 'username', 'email', 'password']


class GenreSerialiser(serializers.Serializer): 
   class Meta:
      model = GenreModel
      fields = ['GenreName'] 

class BookSerialiser(serializers.Serializer): 
   class Meta:
      model = BookModel
      fields = ['BookID','Title','ISBN','PublishedDate','Genre']

class BookDetailsSerialiser(serializers.Serializer):
    class Meta:
        model = BookDetailsModel
        fields = ['DetailsID','BookID','NumberOfPages','Publisher','Language']

class BorrowedBooksSerialiser(serializers.Serializer):
    class Meta:
        model = BorrowedBooks
        fields = ['BookID','BurrowedDate','ReturnDate']


