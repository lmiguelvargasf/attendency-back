from django.contrib import admin

from .models import Member, Project, Meeting, Participation


admin.site.register(Member)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'description', 'team')


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ('project', 'date', 'time')


@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('meeting', 'member', 'attended')
