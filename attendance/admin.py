from django.contrib import admin

from .models import Member, Project


admin.site.register(Member)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'description')
