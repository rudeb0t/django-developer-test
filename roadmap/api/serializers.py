from django.contrib import auth
from rest_framework.serializers import ModelSerializer
from roadmap.models import Project, Roadmap, RoadmapStep


User = auth.get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class RoadmapStepSerializer(ModelSerializer):
    class Meta:
        model = RoadmapStep


class RoadmapSerializer(ModelSerializer):
    steps = RoadmapStepSerializer(many=True)

    class Meta:
        model = Roadmap


class ProjectSerializer(ModelSerializer):
    roadmap = RoadmapSerializer()
    owner = UserSerializer()

    class Meta:
        model = Project
