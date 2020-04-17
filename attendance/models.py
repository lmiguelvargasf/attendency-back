from django.db import models
from django_extensions.db.models import (
    TitleDescriptionModel,
    TimeStampedModel,
)
from django.utils import timezone


class Member(TimeStampedModel):
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64)
    preferred_name = models.CharField(max_length=64, blank=True)
    email = models.EmailField()

    def __str__(self):
        if self.preferred_name:
            return self.preferred_name

        return f'{self.first_name} {self.last_name}'


class Project(TimeStampedModel, TitleDescriptionModel):
    start_date = models.DateField()
    members = models.ManyToManyField(Member,
                                     related_name='projects',
                                     blank=True)

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
    def __localtime(self):
        return timezone.localtime(self.date_time)

    @property
    def date(self):
        return self.__localtime.strftime('%Y-%m-%d')

    @property
    def time(self):
        return self.__localtime.strftime('%H:%M')

    def __str__(self):
        return f'{str(self.project)} meeting on {self.date} at {self.time}'


class Participation(TimeStampedModel):
    meeting = models.ForeignKey(
        Meeting,
        on_delete=models.CASCADE,
        related_name="participations",
        related_query_name="participation",
    )
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name="participations",
        related_query_name="participation",
    )
    observations = models.TextField(blank=True)
    attended = models.BooleanField(default=False)
