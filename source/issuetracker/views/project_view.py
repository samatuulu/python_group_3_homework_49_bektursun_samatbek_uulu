from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from issuetracker.forms import ProjectForm
from issuetracker.models import Project


class ProjectIndexView(ListView):
    template_name = 'project/project_index.html'
    context_object_name = 'project'

    def get_queryset(self):
        return Project.objects.all().order_by('created_at')


class ProjectDetailView(DetailView):
    template_name = 'project/project_detail.html'
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        return Project.objects.all()


class ProjectCreateView(CreateView):
    template_name = 'project/project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})
