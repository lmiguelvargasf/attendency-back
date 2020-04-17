from rest_framework.viewsets import ModelViewSet

from attendance.models import Project, Member, Meeting
from .serializers import (
    ProjectTableSerializer, MemberTableSerializer, MeetingTableSerializer
)


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectTableSerializer


class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberTableSerializer


class MeetingViewSet(ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingTableSerializer
