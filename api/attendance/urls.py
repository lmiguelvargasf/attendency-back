from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (ProjectViewSet, MemberViewSet, MeetingViewSet,
                    SimpleProjectList, MeetingTableList)

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'members', MemberViewSet)
router.register(r'meetings', MeetingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('simple-projects/', SimpleProjectList.as_view()),
    path('meeting-table/', MeetingTableList.as_view()),
]
