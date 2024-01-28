from rest_framework.routers import DefaultRouter

from core.views import RiddleViewSet

router = DefaultRouter()
router.register('riddles', RiddleViewSet, basename='riddle')
urlpatterns = router.urls
