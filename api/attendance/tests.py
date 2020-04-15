import pytest

from attendance.models import Project
from api.attendance.serializers import ProjectTableSerializer

@pytest.fixture
def serializer(project):
    return ProjectTableSerializer(project)


@pytest.mark.django_db
def test_project_table_serializer_has_exected_fields(serializer):
    """Test that ProjectTableSerializer contains expected fields"""
    assert set(serializer.data.keys()) == {
        'key',
        'title',
        'start_date',
        'description',
        'team'
    }

@pytest.mark.django_db
def test_project_table_serializer_key_content(project, serializer):
    """Test that ProjectTableSerializer's key field contains
    the value of Project's id field"""
    assert serializer.data['key'] == project.id
