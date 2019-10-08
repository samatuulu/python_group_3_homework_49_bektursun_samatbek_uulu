from django.views.generic import ListView

from issuetracker.models import Project


class ProjectIndexView(ListView):
    template_name = 'project/project_index.html'
    context_object_name = 'project'

    def get_queryset(self):
        return Project.objects.all().order_by('created_at')