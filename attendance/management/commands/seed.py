import csv
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.utils import timezone

from attendance.models import Member, Project

class Command(BaseCommand):
    help = 'Populates database when it is empty'

    def _populate_db(self):
        User.objects.create_superuser('m', 'm@mathsistor.com', 'pi3.1415')
        current_timezone = timezone.get_current_timezone()
        with open('csv_files/attendance_member.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            Member.objects.bulk_create([Member(**{
                **row,
                'created': timezone.make_aware(
                    datetime.strptime(row['created'], '%Y-%m-%d %H:%M:%S.%f'),
                    current_timezone
                ),
                'modified': timezone.make_aware(
                    datetime.strptime(row['modified'], '%Y-%m-%d %H:%M:%S.%f'),
                    current_timezone
                ),
            }) for row in csv_reader])
        
        with open('csv_files/attendance_project.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            Project.objects.bulk_create([Project(**{
                **row,
                'created': timezone.make_aware(
                    datetime.strptime(row['created'], '%Y-%m-%d %H:%M:%S.%f'),
                    current_timezone
                ),
                'modified': timezone.make_aware(
                    datetime.strptime(row['modified'], '%Y-%m-%d %H:%M:%S.%f'),
                    current_timezone
                ),
            }) for row in csv_reader])


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
