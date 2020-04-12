from django.db import models
from django_extensions.db.models import (
    TitleDescriptionModel,
    TimeStampedModel,
)


class Member(TimeStampedModel):
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64, blank=True, default='')
    last_name = models.CharField(max_length=64)
    preferred_name = models.CharField(max_length=64, blank=True, default='')
    email = models.EmailField()

    def __str__(self):
        if self.preferred_name:
            return self.preferred_name

        return f'{self.first_name} {self.last_name}'


class Project(TimeStampedModel, TitleDescriptionModel):
    start_date = models.DateField()
    members = models.ManyToManyField(Member, related_name='projects')
