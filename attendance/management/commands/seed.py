import csv
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.utils import timezone

from attendance.models import Member, Project


def create_aware_datetime_from_str(datetime_str):
    current_timezone = timezone.get_current_timezone()
    return timezone.make_aware(
        datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S.%f'),
        current_timezone
    )

def create_created_and_modified_dict(d):
    return {
        'created': create_aware_datetime_from_str(d['created']),
        'modified': create_aware_datetime_from_str(d['modified'])
    }

class Command(BaseCommand):
    help = 'Populates database when it is empty'

    def _populate_db(self):
        User.objects.create_superuser('m', 'm@mathsistor.com', 'pi3.1415')
        with open('csv_files/attendance_member.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            Member.objects.bulk_create([Member(
                **{**row, **create_created_and_modified_dict(row)}
            ) for row in csv_reader])
        
        with open('csv_files/attendance_project.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            Project.objects.bulk_create([Project(
                **{**row, **create_created_and_modified_dict(row)}
            ) for row in csv_reader])


    def handle(self, *args, **options):
        try:
            User.objects.get(username='m')
        except User.DoesNotExist:
            self._populate_db()
            self.stdout.write(
                self.style.SUCCESS('Database was successfully populated!')
            )
        else:
            raise CommandError('Database has been already populated.')
