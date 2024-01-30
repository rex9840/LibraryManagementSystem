from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny 

from .serialiser import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = LibraryUser.objects.all()
    serializer_class = UserSerialiser
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']



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

