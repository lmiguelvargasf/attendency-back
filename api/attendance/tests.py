import pytest

from attendance.models import Project
from api.attendance.serializers import (
    ProjectTableSerializer, MemberTableSerializer, MeetingTableSerializer
)


@pytest.fixture
def project_table_serializer(project):
    return ProjectTableSerializer(project)


@pytest.fixture
def member_table_serializer(member):
    return MemberTableSerializer(member)


@pytest.fixture
def meeeting_table_serializer(meeting):
    return MeetingTableSerializer(meeting)


@pytest.mark.django_db
def test_project_table_serializer_has_exected_fields(project_table_serializer):
    """Test that ProjectTableSerializer contains expected fields"""
    assert set(project_table_serializer.data.keys()) == {
        'key', 'title', 'start_date', 'description', 'team'
    }


@pytest.mark.django_db
def test_project_table_serializer_key_content(
    project, project_table_serializer
):
    """Test that ProjectTableSerializer's key field contains
    the value of Project's id field"""
    assert project_table_serializer.data['key'] == project.id


@pytest.mark.django_db
def test_member_table_serializer_has_exected_fields(member_table_serializer):
    """Test that MemberTableSerializer contains expected fields"""
    assert set(member_table_serializer.data.keys()) == {
        'key',
        'first_name',
        'last_name',
        'email',
    }


@pytest.mark.django_db
def test_member_table_serializer_key_content(member, member_table_serializer):
    """Test that MemberTableSerializer's key field contains
    the value of Member's id field"""
    assert member_table_serializer.data['key'] == member.id


@pytest.mark.django_db
def test_meeting_table_serializer_has_exected_fields(meeeting_table_serializer):
    """Test that MeetingTableSerializer contains expected fields"""
    assert set(meeeting_table_serializer.data.keys()) == {
        'key', 'project', 'date', 'time'
    }


@pytest.mark.django_db
def test_meeting_table_serializer_key_content(
    meeting, meeeting_table_serializer
):
    """Test that MeetingTableSerializer's key field contains
    the value of Meetings's id field"""
    assert meeeting_table_serializer.data['key'] == meeting.id


@pytest.mark.django_db
def test_meeting_table_serializer_project_content(
    meeting, meeeting_table_serializer
):
    """Test that MeetingTableSerializer's roject field contains
    the string representation of Meetings's project field"""
    assert meeeting_table_serializer.data['project'] == str(meeting.project)
