from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from attendance.models import Project, Member, Meeting, Participation
from .serializers import (ProjectTableSerializer, MemberTableSerializer,
                          MeetingTableSerializer, SimpleProjectSerializer,
                          MeetingSerializer, ParticipationSerializer)


class SimpleProjectList(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = SimpleProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectTableSerializer


class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberTableSerializer


class MeetingTableList(ListAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingTableSerializer


class MeetingViewSet(ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    @action(detail=True)
    def participation(self, request, pk=None):
        meeting = self.get_object()
        participations = meeting.participations.all()
        participation_serializer = ParticipationSerializer(
            participations, many=True
        )
        data = {
            'participations': participation_serializer.data,
            'observations': meeting.observations
        }

        return Response(data)
