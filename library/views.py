from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny 

from .serialisers  import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = LibraryUser.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserInfoSerialiser
        
        if self.request.method == 'POST':
            return UserSerialiser


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerialiser
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerialiser
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put','delete']


class BookDetailsViewSet(viewsets.ModelViewSet): 
    queryset = BookDetail.objects.all()    
    serializer_class = BookDetailsSerialiser
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put','delete']

class BorrowedBooksViewSet(viewsets.ModelViewSet):
    queryset = UserBorrowedBook.objects.all()
    serializer_class = UserBorrowedBookSerialiser
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put','delete']





class SubmitBookViewSet(viewsets.ModelViewSet):
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBooksSerialiser
    permission_classes = [IsAuthenticated]
    http_method_names = ['delete','get']


    def destroy(self,request,pk): 
        try:
            borrowed_book = BorrowedBook.objects.get(pk=pk)
            borrowed_book.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        except BorrowedBook.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

