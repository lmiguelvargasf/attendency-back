from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Meeting, Participation


@receiver(post_save, sender=Meeting)
def create_meeting_participations(sender, instance, created, **kwargs):
    if created:
        for member in instance.project.members.all():
            Participation.objects.create(meeting=instance,member=member)
