from django.views.generic import ListView

from issuetracker.models import Team


class TeamIndexView(ListView):
    template_name = 'team/team_index.html'
    context_object_name = 'teams'

    def get_queryset(self):
        return Team.objects.all()