from rest_framework.viewsets import ModelViewSet

from attendance.models import Project, Member
from .serializers import ProjectTableSerializer, MemberTableSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectTableSerializer


class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberTableSerializer
