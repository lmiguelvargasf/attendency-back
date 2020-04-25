from rest_framework import serializers

from attendance.models import Project, Member, Meeting


class BaseReactModelSerializer(serializers.HyperlinkedModelSerializer):
    key = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        abstract = True
        fields = ('key', 'url')


class SimpleProjectSerializer(BaseReactModelSerializer):
    class Meta:
        model = Project
        fields = BaseReactModelSerializer.Meta.fields + ('title', )


class ProjectTableSerializer(BaseReactModelSerializer):
    class Meta:
        model = Project
        fields = BaseReactModelSerializer.Meta.fields + (
            'title', 'start_date', 'description', 'team', 'members'
        )
        extra_kwargs = {'members': {'write_only': True}}


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
