from .views import * 
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user',UserViewSet,basename='user')
router.register('genre',GenreViewSet,basename='genre') 
router.register('book',BookViewSet,basename='book')
router.register('bookdetails',BookDetailsViewSet,basename='bookdetails') 
router.register('borrowedbooks',BorrowedBooksViewSet,basename='borrowedbooks') 
router.register('submitbook',SubmitBookViewSet,basename='submitbook')


route_url = router.urls
