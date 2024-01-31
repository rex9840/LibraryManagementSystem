from .views import * 
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users',UserViewSet,basename='user')
router.register('genres',GenreViewSet,basename='genre') 
router.register('books',BookViewSet,basename='book')
router.register('bookdetails',BookDetailsViewSet,basename='bookdetails') 
router.register('borrowedbooks',BorrowedBooksViewSet,basename='borrowedbooks') 
router.register('submitborrowedbook',SubmitBookViewSet,basename='submitbook')


route_url = router.urls
