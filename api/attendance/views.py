from rest_framework.viewsets import ModelViewSet

from attendance.models import Project
from .serializers import ProjectTableSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectTableSerializer
