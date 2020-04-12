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
def test_str_project():
    """Test that title is returned as string representation of Member model"""
    start_date = datetime.strptime('2020-04-12', '%Y-%m-%d').date()
    project = Project.objects.create(title='My Project', start_date=start_date)

    assert str(project) == 'My Project'
