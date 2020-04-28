from datetime import datetime

from django.urls import reverse
from django.utils import timezone
from rest_framework.status import HTTP_200_OK
from rest_framework.utils.serializer_helpers import ReturnList

import pytest

from attendance.models import Project, Meeting, Member
from api.attendance.serializers import ParticipationSerializer


@pytest.mark.django_db
def test_participation_view_no_participations_no_observations(client, project):
    """Test that participation view in MeetingViewSet returns 200 reponse,
    data has participations which is an empty list, and observations which is a string
    which is empty"""
    project.members.clear()
    date_time = datetime.strptime('2020-04-12 17:30', '%Y-%m-%d %H:%M')
    date_time = timezone.make_aware(date_time,
                                    timezone=timezone.get_current_timezone())
    meeting = Meeting.objects.create(project=project, date_time=date_time)

    url = reverse('meeting-participation', kwargs={'pk': meeting.pk})
    response = client.get(url)
    data = response.data

    assert response.status_code == HTTP_200_OK
    assert type(data['participations']) == ReturnList
    assert data['participations'] == []
    assert type(data['observations']) is str
    assert data['observations'] == ''


@pytest.mark.django_db
def test_participation_view_one_participation_and_observations(
    client, meeting, member):
    """Test that participation view in MeetingViewSet returns 200 reponse,
    data has participations which is a list with one element, and observations
    which is a non-empty string"""
    meeting.observations = 'This is for testing purposes.'
    meeting.save()
    url = reverse('meeting-participation', kwargs={'pk': meeting.pk})
    response = client.get(url)
    data = response.data

    assert response.status_code == HTTP_200_OK
    assert len(data['participations']) == 1
    assert data['participations'][0] == ParticipationSerializer(
        meeting.participations.first()).data
    assert data['observations'] == meeting.observations


@pytest.mark.django_db
def test_participation_view_two_participation_and_observations(
    client, project, member, serializer_context):
    """Test that participation view in MeetingViewSet returns 200 reponse,
    data has participations which is a list with two elements, and observations
    which is a non-empty string"""
    another_member = Member.objects.create(
        first_name='Peter',
        last_name='Smith',
        email='peter.smith@example.com',
    )
    project.members.add(another_member)
    date_time = datetime.strptime('2020-04-12 17:30', '%Y-%m-%d %H:%M')
    date_time = timezone.make_aware(date_time,
                                    timezone=timezone.get_current_timezone())
    meeting = Meeting.objects.create(project=project, date_time=date_time)

    url = reverse('meeting-participation', kwargs={'pk': meeting.pk})
    response = client.get(url)
    data = response.data
    participations = meeting.participations.all()

    assert response.status_code == HTTP_200_OK
    assert len(data['participations']) == 2
    assert data['participations'][0] == ParticipationSerializer(
        participations[0]).data
    assert data['participations'][1] == ParticipationSerializer(
        participations[1]).data
    assert data['observations'] == meeting.observations
