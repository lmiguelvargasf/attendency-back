from django.db import models
from django_extensions.db.models import TimeStampedModel


class Member(TimeStampedModel):
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64, blank=True, default='')
    last_name = models.CharField(max_length=64)
    preferred_name = models.CharField(max_length=64, blank=True, default='')
    email = models.EmailField()

    def __str__(self):
        return self.preferred_name
