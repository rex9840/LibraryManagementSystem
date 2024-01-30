from django.urls import path,include
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('user',UserViewSet,basename='user')
router.register('genre',GenreViewSet,basename='genre') 
router.register('book',BookViewSet,basename='book')
router.register('bookdetails',BookDetailsViewSet,basename='bookdetails') 
router.register('borrowedbooks',BorrowedBooksViewSet,basename='borrowedbooks') 



urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]



urlpatterns += router.urls



