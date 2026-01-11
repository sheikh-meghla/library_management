from rest_framework.routers import DefaultRouter
from .views import BookViewSet, MemberViewSet, IssueBookViewSet, CategoryViewSet

router = DefaultRouter()


router.register('categories', CategoryViewSet)

router.register('books', BookViewSet)
router.register('members', MemberViewSet)
router.register('issues', IssueBookViewSet)

urlpatterns = router.urls
