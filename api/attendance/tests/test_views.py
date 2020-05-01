from datetime import datetime
import json

from django.urls import reverse
from django.utils import timezone
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIClient
from rest_framework.utils.serializer_helpers import ReturnList

import pytest

from attendance.models import Project, Meeting, Member
from api.attendance.serializers import ParticipationSerializer

@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_all_members_when_no_members_in_project(api_client, project, member):
    """Test that all existing members are retrieved when calling service
    non-members if project has no members"""
    project.members.clear()
    url = reverse('project-non-members', kwargs={'pk': project.pk})
    response = api_client.get(url)
    data = response.data

    assert response.status_code == HTTP_200_OK
    assert len(data) == 1
    assert data[0]['key'] == member.id


@pytest.mark.django_db
def test_remaining_members_when_some_members_in_project(api_client, project):
    """Test that remaining members are retried when calling service
    non-members if project has already some members"""
    new_member = Member.objects.create(first_name='Peter',
                                       last_name='Jones',
                                       email='peter.jones@gmail.com')

    url = reverse('project-non-members', kwargs={'pk': project.pk})
    response = api_client.get(url)
    data = response.data

    assert response.status_code == HTTP_200_OK
    assert len(data) == 1
    assert data[0]['key'] == new_member.id


@pytest.mark.django_db
def test_no_members_when_all_members_in_project(api_client, project):
    """Test that no members are retrieve when calling service
    non-members if all members are already in project"""
    url = reverse('project-non-members', kwargs={'pk': project.pk})
    response = api_client.get(url)
    data = response.data
    assert response.status_code == HTTP_200_OK
    assert len(data) == 0


@pytest.mark.django_db
def test_participation_view_no_participations_no_observations(api_client, project):
    """Test that participation view in MeetingViewSet returns 200 reponse,
    data has participations which is an empty list, and observations which is a string
    which is empty"""
    project.members.clear()
    date_time = datetime.strptime('2020-04-12 17:30', '%Y-%m-%d %H:%M')
    date_time = timezone.make_aware(date_time,
                                    timezone=timezone.get_current_timezone())
    meeting = Meeting.objects.create(project=project, date_time=date_time)

    url = reverse('meeting-participation', kwargs={'pk': meeting.pk})
    response = api_client.get(url)
    data = response.data

    assert response.status_code == HTTP_200_OK
    assert type(data['participations']) == ReturnList
    assert data['participations'] == []
    assert type(data['observations']) is str
    assert data['observations'] == ''


@pytest.mark.django_db
def test_participation_view_one_participation_and_observations(
    api_client, meeting, member):
    """Test that participation view in MeetingViewSet returns 200 reponse,
    data has participations which is a list with one element, and observations
    which is a non-empty string"""
    meeting.observations = 'This is for testing purposes.'
    meeting.save()
    url = reverse('meeting-participation', kwargs={'pk': meeting.pk})
    response = api_client.get(url)
    data = response.data

    assert response.status_code == HTTP_200_OK
    assert len(data['participations']) == 1
    assert data['participations'][0] == ParticipationSerializer(
        meeting.participations.first()).data
    assert data['observations'] == meeting.observations


@pytest.mark.django_db
def test_participation_view_two_participation_and_observations(
    api_client, project, member, serializer_context):
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
    response = api_client.get(url)
    data = response.data
    participations = meeting.participations.all()

    assert response.status_code == HTTP_200_OK
    assert len(data['participations']) == 2
    assert data['participations'][0] == ParticipationSerializer(
        participations[0]).data
    assert data['participations'][1] == ParticipationSerializer(
        participations[1]).data
    assert data['observations'] == meeting.observations


@pytest.mark.django_db
@pytest.mark.parametrize('attended', [True, False])
def test_track_participation_updates_attended_in_participation_and_observations_in_meeting(
    api_client, meeting, attended):
    """Test that track_participation view in MeetingViewSet returns 200 response,
    and it also updates the value of attended field in Participation instance
    and the value of observations field in Meeting instance"""
    url = reverse('meeting-track-participation', kwargs={'pk': meeting.pk})
    participation = meeting.participations.first()
    data = {
        'participations': [{
            'key': participation.id,
            'attended': attended
        }],
        'observations': 'This is just a test.'
    }
    response = api_client.post(url, data, format='json')
    participation.refresh_from_db()
    meeting.refresh_from_db()

    assert response.status_code == HTTP_200_OK
    assert participation.attended == attended
    assert meeting.observations == 'This is just a test.'
