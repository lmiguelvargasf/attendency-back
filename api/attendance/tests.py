import pytest

from attendance.models import Project
from api.attendance.serializers import ProjectTableSerializer, MemberTableSerializer


@pytest.fixture
def project_table_serializer(project):
    return ProjectTableSerializer(project)


@pytest.fixture
def member_table_serializer(member):
    return MemberTableSerializer(member)


@pytest.mark.django_db
def test_project_table_serializer_has_exected_fields(project_table_serializer):
    """Test that ProjectTableSerializer contains expected fields"""
    assert set(project_table_serializer.data.keys()) == {
        'key', 'title', 'start_date', 'description', 'team'
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
        'first_name',
        'last_name',
        'email',
    }


@pytest.mark.django_db
def test_member_table_serializer_key_content(member, member_table_serializer):
    """Test that MemberTableSerializer's key field contains
    the value of Member's id field"""
    assert member_table_serializer.data['key'] == member.id
