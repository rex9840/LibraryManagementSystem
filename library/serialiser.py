from django.db.models.expressions import fields
from rest_framework import serializers
from .models import LibraryUser,Genre,Book,BookDetail,BorrowedBook,UserBorrowedBook


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = LibraryUser
        fields = '__all__' 

class GenreSerialiser(serializers.Serializer):
   genre_name = serializers.CharField(max_length=100)
   class Meta:
      model = Genre
      fields = '__all__'

class BookSerialiser(serializers.ModelSerializer): 
    genre = GenreSerialiser(many=True)
    class Meta:
      model = Book
      fields = '__all__'

class BookDetailsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = BookDetail
        fields ='__all__'

class BorrowedBooksSerialiser(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBook
        fields =   '__all__' 


class UserBorrowedBookSerialiser(serializers.ModelSerializer):
    burrowed_books = BorrowedBooksSerialiser(many=True)
    class Meta:
        model = UserBorrowedBook
        fields =   '__all__'
        

