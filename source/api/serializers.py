from rest_framework import serializers

from issuetracker.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'tittle', 'description', 'created_at', 'updated_at', 'status')