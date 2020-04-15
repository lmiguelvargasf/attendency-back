from datetime import datetime

from django.utils import timezone

import pytest

from attendance.models import Member, Project, Meeting, Participation

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