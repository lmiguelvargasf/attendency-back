import pytest

from .models import Member


@pytest.mark.django_db
def test_str_member_when_no_preferred_name():
    """Test that concatenation of first and last names is
    returned as string representation when no preferred name
    is provided"""
    member = Member.objects.create(
        first_name='John',
        last_name='Doe',
        email='john.doe@example.com',
    )

    assert str(member) == 'John Doe'


@pytest.mark.django_db
def test_str_member_when_preferred_name():
    """Test that preferred name is returned as string representation
    when preferred name is provided"""
    member = Member.objects.create(
        first_name='John',
        last_name='Doe',
        preferred_name='JD',
        email='john.doe@example.com',
    )

    assert str(member) == 'JD'
