from rest_framework import serializers

from attendance.models import Project, Member, Meeting


class ProjectTableSerializer(serializers.ModelSerializer):
    key = serializers.IntegerField(source='id')

    class Meta:
        model = Project
        fields = ('key', 'title', 'start_date', 'description', 'team')


class MemberTableSerializer(serializers.ModelSerializer):
    key = serializers.IntegerField(source='id')

    class Meta:
        model = Member
        fields = ('key', 'first_name', 'last_name', 'email')


class MeetingTableSerializer(serializers.ModelSerializer):
    key = serializers.IntegerField(source='id')
    project = serializers.CharField()

    class Meta:
        model = Meeting
        fields = ('key', 'project', 'date', 'time')
