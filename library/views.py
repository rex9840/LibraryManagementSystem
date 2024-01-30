from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny 

from .serialiser import *
from .models import *

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = LibraryUserSerialiser
    queryset = LibraryUser.objects.all()
    permission_classes = [IsAuthenticated]


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerialiser
    queryset = GenreModel.objects.all()
    permission_classes = [IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet): 
    serializer_class = BookSerialiser
    queryset = BookModel.objects.all()
    permission_classes = [IsAuthenticated]


class BookDetailsViewSet(viewsets.ModelViewSet): 
    serializer_class = BookDetailsSerialiser
    queryset = BookDetailsModel.objects.all()
    permission_classes = [IsAuthenticated]


class BorrowedBooksViewSet(viewsets.ModelViewSet):
    serializer_class = BorrowedBooksSerialiser
    queryset = BorrowedBooks.objects.all()
    permission_classes = [IsAuthenticated]






