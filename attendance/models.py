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
    members = models.ManyToManyField(Member, related_name='projects', blank=True)

    def __str__(self):
        return self.title
    
    @property
    def team(self):
        return ', '.join(str(member) for member in self.members.all())


class Meeting(TimeStampedModel):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="meetings",
        related_query_name="meeting",
    )
    date_time = models.DateTimeField()

    @property
    def time(self):
        return self.date_time.strftime('%H:%M')


    @property
    def date(self):
        return self.date_time.strftime('%Y-%m-%d')

    def __str__(self):
        return f'{str(self.project)} meeting on {self.date} at {self.time}'
