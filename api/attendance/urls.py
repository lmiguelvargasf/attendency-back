from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet, MemberViewSet, MeetingViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'members', MemberViewSet)
router.register(r'meetings', MeetingViewSet)

urlpatterns = router.urls
