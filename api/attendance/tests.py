import pytest

from attendance.models import Project
from api.attendance.serializers import (ProjectTableSerializer,
                                        MemberTableSerializer,
                                        MeetingTableSerializer,
                                        SimpleProjectSerializer,
                                        MeetingSerializer)


@pytest.fixture
def simple_project_serializer(project, serializer_context):
    return SimpleProjectSerializer(project, context=serializer_context)


@pytest.fixture
def project_table_serializer(project, serializer_context):
    return ProjectTableSerializer(project, context=serializer_context)


@pytest.fixture
def member_table_serializer(member, serializer_context):
    return MemberTableSerializer(member, context=serializer_context)


@pytest.fixture
def meeeting_table_serializer(meeting, serializer_context):
    return MeetingTableSerializer(meeting, context=serializer_context)


@pytest.fixture
def meeting_serializer(meeting, serializer_context):
    return MeetingSerializer(meeting, context=serializer_context)


@pytest.mark.django_db
def test_simple_project_serializer_has_expected_fields(
    simple_project_serializer):
    """Test that SimpleProjectSerializer contains expected fields"""
    assert set(simple_project_serializer.data.keys()) == {'key', 'url', 'title'}


@pytest.mark.django_db
def test_simple_project_serializer_key_content(project,
                                               simple_project_serializer):
    """Test that SimpleProjectSerializer's key field contains
    the value of Project's id field"""
    assert simple_project_serializer.data['key'] == project.id


@pytest.mark.django_db
def test_project_table_serializer_has_exected_fields(project_table_serializer):
    """Test that ProjectTableSerializer contains expected fields"""
    assert set(project_table_serializer.data.keys()) == {
        'key', 'url', 'title', 'start_date', 'description', 'team'
    }


@pytest.mark.django_db
def test_project_table_serializer_key_content(project,
                                              project_table_serializer):
    """Test that ProjectTableSerializer's key field contains
    the value of Project's id field"""
    assert project_table_serializer.data['key'] == project.id


@pytest.mark.django_db
def test_member_table_serializer_has_exected_fields(member_table_serializer):
    """Test that MemberTableSerializer contains expected fields"""
    assert set(member_table_serializer.data.keys()) == {
        'key',
        'url',
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
def test_meeting_serializer_has_exected_fields(meeting_serializer):
    """Test that MeetingSerializer contains expected fields"""
    assert set(meeting_serializer.data.keys()) == {
        'key', 'url', 'project', 'date_time'
    }


@pytest.mark.django_db
def test_meeting_serializer_key_content(meeting, meeting_serializer):
    """Test that MeetingSerializer's key field contains
    the value of Meetings's id field"""
    assert meeting_serializer.data['key'] == meeting.id


@pytest.mark.django_db
def test_meeting_table_serializer_has_exected_fields(meeeting_table_serializer):
    """Test that MeetingTableSerializer contains expected fields"""
    assert set(meeeting_table_serializer.data.keys()) == {
        'key', 'url', 'project', 'project_title', 'date', 'time'
    }


@pytest.mark.django_db
def test_meeting_table_serializer_key_content(meeting,
                                              meeeting_table_serializer):
    """Test that MeetingTableSerializer's key field contains
    the value of Meetings's id field"""
    assert meeeting_table_serializer.data['key'] == meeting.id


@pytest.mark.django_db
def test_meeting_table_serializer_project_title_content(meeting,
                                                  meeeting_table_serializer):
    """Test that MeetingTableSerializer's project_title field contains
    the string representation of Meetings's project field"""
    assert meeeting_table_serializer.data['project_title'] == str(meeting.project)
