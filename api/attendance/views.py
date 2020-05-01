from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from attendance.models import Project, Member, Meeting, Participation
from .serializers import (ProjectSerializer, MemberTableSerializer,
                          MeetingTableSerializer, SimpleProjectSerializer,
                          MeetingSerializer, ParticipationSerializer)


class SimpleProjectList(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = SimpleProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


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

    @action(detail=True, methods=['post'], url_path='track-participation')
    def track_participation(self, request, pk=None):
        meeting = self.get_object()
        data = request.data

        for p in data['participations']:
            participation = Participation.objects.get(id=p['key'])
            participation.attended = p['attended']
            participation.save()
        meeting.observations = data['observations']
        meeting.save()

        return Response()
