from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from attendance.models import Project, Member, Meeting
from .serializers import (ProjectTableSerializer, MemberTableSerializer,
                          MeetingTableSerializer, SimpleProjectSerializer)


class SimpleProjectList(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = SimpleProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectTableSerializer


class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberTableSerializer


class MeetingViewSet(ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingTableSerializer
