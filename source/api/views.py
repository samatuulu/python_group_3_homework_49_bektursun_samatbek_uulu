from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS

from issuetracker.models import Project, Task
from api.serializers import ProjectSerializer, TaskSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()
