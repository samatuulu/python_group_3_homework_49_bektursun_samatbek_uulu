from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        obj = self.get_object()
        context = super().get_context_data(**kwargs)
        context[self.context_object_name] = obj
        context['tasks'] = obj.task_project.all().order_by('-created_at')
        return context

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return get_object_or_404(self.model, pk=pk)


class ProjectCreateView(CreateView):
    template_name = 'project/project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectUpdateView(UpdateView):
    template_name = 'project/project_update.html'
    model = Project
    context_object_name = 'project'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    template_name = 'project/project_delete.html'
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('project_index')