from django.views.generic import ListView

from issuetracker.models import Team, Project


class TeamIndexView(ListView):
    model = Project
    template_name = 'team/team_index.html'
    context_object_name = 'projects'