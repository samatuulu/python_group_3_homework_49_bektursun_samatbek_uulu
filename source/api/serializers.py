from rest_framework import serializers

from issuetracker.models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'tittle', 'description', 'created_at', 'updated_at', 'status')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id', 'summary', 'description', 'status', 'type',
            'project', 'created_at',
            'created_by', 'assigned_to'
        )