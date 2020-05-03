from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet

from attendance.models import Project, Member, Meeting, Participation
from .serializers import (ProjectSerializer, MemberSerializer,
                          MeetingTableSerializer, SimpleProjectSerializer,
                          MeetingSerializer, ParticipationSerializer)


class SimpleProjectList(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = SimpleProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(detail=True, url_path='non-members')
    def non_members(self, request, pk=None):
        project = self.get_object()
        non_members = Member.objects.exclude(id__in=project.members.all())
        member_serializer = MemberSerializer(
            non_members, many=True, context=self.get_serializer_context())

        return Response(member_serializer.data)
    
    @action(detail=True)
    def members(self, request, pk=None):
        project = self.get_object()
        member_serializer = MemberSerializer(
            project.members.all(), many=True, context=self.get_serializer_context())

        return Response(member_serializer.data)

    @action(detail=True, methods=['post'], url_path='add-member')
    def add_member(self, request, pk=None):
        project = self.get_object()

        try:
            member = Member.objects.get(id=request.data['key'])
        except Member.DoesNotExist:
            return Response({'error': 'Member does not exists'},
                            status=HTTP_400_BAD_REQUEST)

        if member in project.members.all():
            return Response({'error': 'Member already in project'},
                            status=HTTP_400_BAD_REQUEST)

        project.members.add(member)
        project_serializer = self.serializer_class(
            project, context=self.get_serializer_context())
        return Response(project_serializer.data)
    
    @action(detail=True, methods=['post'], url_path='remove-member')
    def remove_member(self, request, pk=None):
        project = self.get_object()

        try:
            member = Member.objects.get(id=request.data['key'])
        except Member.DoesNotExist:
            return Response({'error': 'Member does not exists'},
                            status=HTTP_400_BAD_REQUEST)

        if member not in project.members.all():
            return Response({'error': 'Member is not in project'},
                            status=HTTP_400_BAD_REQUEST)

        project.members.remove(member)
        project_serializer = self.serializer_class(
            project, context=self.get_serializer_context())
        return Response(project_serializer.data)


class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


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
        participation_serializer = ParticipationSerializer(participations,
                                                           many=True)
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
