import pytest

from api.attendance.serializers import (
    ProjectSerializer, MemberSerializer, MeetingTableSerializer,
    SimpleProjectSerializer, MeetingSerializer, ParticipationSerializer)


@pytest.fixture
def simple_project_serializer(project, serializer_context):
    return SimpleProjectSerializer(project, context=serializer_context)


@pytest.fixture
def project_serializer(project, serializer_context):
    return ProjectSerializer(project, context=serializer_context)


@pytest.fixture
def member_serializer(member, serializer_context):
    return MemberSerializer(member, context=serializer_context)


@pytest.fixture
def meeeting_table_serializer(meeting, serializer_context):
    return MeetingTableSerializer(meeting, context=serializer_context)


@pytest.fixture
def meeting_serializer(meeting, serializer_context):
    return MeetingSerializer(meeting, context=serializer_context)


@pytest.fixture
def participation_serializer(participation):
    return ParticipationSerializer(participation)


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
def test_project_serializer_has_exected_fields(project_serializer):
    """Test that ProjectSerializer contains expected fields"""
    assert set(project_serializer.data.keys()) == {
        'key', 'url', 'title', 'start_date', 'description', 'team'
    }


@pytest.mark.django_db
def test_project_serializer_key_content(project,
                                              project_serializer):
    """Test that ProjectSerializer's key field contains
    the value of Project's id field"""
    assert project_serializer.data['key'] == project.id


@pytest.mark.django_db
def test_member_serializer_has_exected_fields(member_serializer):
    """Test that MemberSerializer contains expected fields"""
    assert set(member_serializer.data.keys()) == {
        'key',
        'url',
        'first_name',
        'middle_name',
        'last_name',
        'preferred_name',
        'email',
    }


@pytest.mark.django_db
def test_member_serializer_key_content(member, member_serializer):
    """Test that MemberSerializer's key field contains
    the value of Member's id field"""
    assert member_serializer.data['key'] == member.id


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
def test_meeting_table_serializer_project_title_content(
    meeting, meeeting_table_serializer):
    """Test that MeetingTableSerializer's project_title field contains
    the string representation of Meetings's project field"""
    assert meeeting_table_serializer.data['project_title'] == str(
        meeting.project)


@pytest.mark.django_db
def test_participation_serializer_has_expected_fields(participation_serializer):
    """Test that ParticipationSerializer contains expected fields"""
    assert set(participation_serializer.data.keys()) == {
        'key', 'meeting', 'member', 'member_name', 'attended'
    }


@pytest.mark.django_db
def test_participation_serializer_key_content(participation,
                                              participation_serializer):
    """Test that ParticipationSerializer's key field contains the value of
    Participation's id field"""
    assert participation_serializer.data['key'] == participation.id


@pytest.mark.django_db
def test_participation_serializer_member_name_content(participation,
                                                      participation_serializer):
    """Test that ParticipationSerializer's member_name field contains the value
    of Participations's member's preferred_name field"""
    assert participation_serializer.data[
        'member_name'] == participation.member.preferred_name
