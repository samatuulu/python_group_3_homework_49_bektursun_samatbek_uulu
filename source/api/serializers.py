from rest_framework import serializers

from issuetracker.models import Project, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id', 'summary', 'description', 'status', 'type',
            'project', 'created_at',
            'created_by', 'assigned_to'
        )


class ProjectSerializer(serializers.ModelSerializer):
    task_project = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ('id', 'tittle', 'description', 'created_at', 'updated_at', 'status', 'task_project')

