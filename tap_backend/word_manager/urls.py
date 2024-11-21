from rest_framework.routers import DefaultRouter
from .views import WordListViewSet, WordViewSet

router = DefaultRouter()
router.register(r'word-lists', WordListViewSet, basename='word-list')
router.register(r'words', WordViewSet, basename='word')

urlpatterns = router.urls
