from rest_framework.viewsets import ModelViewSet
from roadmap.api.serializers import ProjectSerializer
from roadmap.models import Project


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
