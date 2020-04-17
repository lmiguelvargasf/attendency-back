from rest_framework import serializers

from attendance.models import Project, Member, Meeting


class BaseReactModelSerializer(serializers.ModelSerializer):
    key = serializers.IntegerField(source='id')

    class Meta:
        abstract = True
        fields = ('key',)


class ProjectTableSerializer(BaseReactModelSerializer):
    class Meta:
        model = Project
        fields = BaseReactModelSerializer.Meta.fields + (
            'title', 'start_date', 'description', 'team'
        )


class MemberTableSerializer(BaseReactModelSerializer):
    class Meta:
        model = Member
        fields = BaseReactModelSerializer.Meta.fields + (
            'key', 'first_name', 'last_name', 'email'
        )


class MeetingTableSerializer(BaseReactModelSerializer):
    project = serializers.CharField()

    class Meta:
        model = Meeting
        fields = BaseReactModelSerializer.Meta.fields + (
            'key', 'project', 'date', 'time'
        )
