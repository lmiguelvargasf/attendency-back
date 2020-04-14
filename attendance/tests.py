from datetime import datetime

from django.utils import timezone

import pytest

from .models import Member, Project, Meeting, Participation

@pytest.fixture
def member():
    return Member.objects.create(
        first_name='John',
        last_name='Doe',
        email='john.doe@example.com',
    )

@pytest.fixture
def project(member):
    start_date = datetime.strptime('2020-04-12', '%Y-%m-%d').date()
    project = Project.objects.create(title='My Project', start_date=start_date)
    project.members.add(member)

    return project


@pytest.fixture
def meeting(project):
    date_time = datetime.strptime('2020-04-12 17:30', '%Y-%m-%d %H:%M')
    date_time = timezone.make_aware(date_time, timezone=timezone.get_current_timezone())
    return Meeting.objects.create(
        project=project,
        date_time=date_time
    )


@pytest.mark.django_db
def test_str_member_when_no_preferred_name(member):
    """Test that concatenation of first and last names is
    returned as string representation of Member instance when no
    preferred name is provided"""
    assert str(member) == 'John Doe'


@pytest.mark.django_db
def test_str_member_when_preferred_name(member):
    """Test that preferred name is returned as string representation
    of Member instance when preferred name is provided"""
    member.preferred_name = 'JD'
    member.save()

    assert str(member) == 'JD'

@pytest.mark.django_db
def test_str_project(project):
    """Test that title is returned as string representation of Member model"""
    assert str(project) == 'My Project'

@pytest.mark.django_db
def test_project_with_no_member_returns_empty_str_as_team(project, member):
    """Test that empty string is returned when a Project instance
    has no member assinged."""
    project.members.remove(member)
    assert project.team == ''

@pytest.mark.django_db
def test_project_with_one_member_returns_member_str(project, member):
    """Test that Member's string representation is returned when a Project
    instance only one member assinged."""
    assert project.team == 'John Doe'


@pytest.mark.django_db
def test_project_with_two_members_returns_member_str_joined_with_commas(
    project
):
    """Test that Members' string representation joined by commans is returned when
    a Project instance two members assinged."""
    another_member = Member.objects.create(
        first_name='Peter',
        last_name='Smith',
        email='peter.smith@exaple.com'
    )
    project.members.add(another_member)
    assert project.team == 'Peter Smith, John Doe'


@pytest.mark.django_db
def test_meeting_time(meeting):
    """Test that time for meeting is returned properly in format HH:MM"""
    assert meeting.time == '17:30'

@pytest.mark.django_db
def test_meeting_date(meeting):
    """Test that date for meeting is returned properly in format YYYY-MM-DD"""
    assert meeting.date == '2020-04-12'


@pytest.mark.django_db
def test_str_meeting(meeting):
    """Test that string representation for Meeting instance
    is returned properly"""
    assert str(meeting) == 'My Project meeting on 2020-04-12 at 17:30'

@pytest.mark.django_db
def test_participation_is_created_when_meeting_is_created(meeting, member):
    """Test that Participation instance with attended field as False is associated with
    meeting and member is created when a meeting is created"""
    queryset = Participation.objects.all()

    assert len(queryset) == 1
    participation = queryset.first()
    assert participation.member == member
    assert participation.meeting == meeting
    assert not participation.attended
