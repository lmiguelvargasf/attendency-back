from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet, MemberViewSet


router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'members', MemberViewSet)

urlpatterns = router.urls
