from rest_framework import serializers

from attendance.models import Project, Member, Meeting, Participation


class BaseReactModelSerializer(serializers.HyperlinkedModelSerializer):
    key = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        abstract = True
        fields = ('key', 'url')


class SimpleProjectSerializer(BaseReactModelSerializer):

    class Meta:
        model = Project
        fields = BaseReactModelSerializer.Meta.fields + ('title',)


class ProjectSerializer(BaseReactModelSerializer):

    class Meta:
        model = Project
        fields = BaseReactModelSerializer.Meta.fields + (
            'title', 'start_date', 'description', 'team', 'members')
        extra_kwargs = {'members': {'write_only': True}}


class MemberSerializer(BaseReactModelSerializer):

    class Meta:
        model = Member
        fields = BaseReactModelSerializer.Meta.fields + (
            'first_name',
            'middle_name',
            'last_name',
            'preferred_name',
            'email')


class MeetingSerializer(BaseReactModelSerializer):

    class Meta:
        model = Meeting
        fields = BaseReactModelSerializer.Meta.fields + ('project', 'date_time')


class MeetingTableSerializer(BaseReactModelSerializer):
    project_title = serializers.CharField(source='project', read_only=True)

    class Meta:
        model = Meeting
        fields = BaseReactModelSerializer.Meta.fields + (
            'project',
            'project_title',
            'date',
            'time',
        )


class ParticipationSerializer(serializers.ModelSerializer):
    key = serializers.IntegerField(source='id', read_only=True)
    member_name = serializers.CharField(source='member.preferred_name',
                                        read_only=True)

    class Meta:
        model = Participation
        fields = ('key', 'meeting', 'member', 'member_name', 'attended')
