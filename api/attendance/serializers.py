from rest_framework import serializers

from attendance.models import Project, Member, Meeting


class BaseReactModelSerializer(serializers.HyperlinkedModelSerializer):
    key = serializers.IntegerField(source='id')

    class Meta:
        abstract = True
        fields = ('key', 'url')


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
            'first_name', 'last_name', 'email'
        )


class MeetingTableSerializer(BaseReactModelSerializer):
    project = serializers.CharField()

    class Meta:
        model = Meeting
        fields = BaseReactModelSerializer.Meta.fields + (
            'project',
            'date',
            'time',
        )
