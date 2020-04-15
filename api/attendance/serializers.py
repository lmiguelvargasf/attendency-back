from rest_framework import serializers

from attendance.models import Project

class ProjectTableSerializer(serializers.ModelSerializer):
    key = serializers.IntegerField(source='id')
    class Meta:
        model = Project
        fields = ('key', 'title', 'start_date', 'description', 'team')
