from datetime import datetime
import pytest

from .models import Member, Project

@pytest.fixture
def member():
    return Member.objects.create(
        first_name='John',
        last_name='Doe',
        email='john.doe@example.com',
    )

@pytest.fixture
def project():
    start_date = datetime.strptime('2020-04-12', '%Y-%m-%d').date()
    return Project.objects.create(title='My Project', start_date=start_date)



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
def test_project_with_no_member_returns_empty_str_as_team(project):
    """Test that empty string is returned when a Project instance
    has no member assinged."""
    assert project.team == ''

@pytest.mark.django_db
def test_project_with_one_member_returns_member_str(project, member):
    """Test that Member's string representation is returned when a Project
    instance only one member assinged."""
    project.members.add(member)
    assert project.team == 'John Doe'


@pytest.mark.django_db
def test_project_with_two_members_returns_member_str_joined_with_commas(
    project,
    member
):
    """Test that Members' string representation joined by commans is returned when
    a Project instance two members assinged."""
    another_member = Member.objects.create(
        first_name='Peter',
        last_name='Smith',
        email='peter.smith@exaple.com'
    )
    project.members.add(member, another_member)
    assert project.team == 'Peter Smith, John Doe'
