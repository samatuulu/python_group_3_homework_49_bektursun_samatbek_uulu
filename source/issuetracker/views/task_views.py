from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView

from issuetracker.forms import TaskForm
from issuetracker.models import Task
from .base_view import DetailView, UpdateView, DeleteView


class IndexView(ListView):
    template_name = 'task/index.html'
    context_object_name = 'tasks'
    paginate_by = 2
    paginate_orphans = 1

    def get_queryset(self):
        return Task.objects.all().order_by('-created_at')


class TaskView(DetailView):
    template_name = 'task/task_detail.html'
    model = Task
    context_key = 'task'


class TaskCreateView(CreateView):
    template_name = 'task/task_create.html'
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('index')


class TaskUpdateView(UpdateView):
    template_name = 'task/task_update.html'
    model = Task
    form_class = TaskForm
    context_object_name = 'task'

    def get_redirect_url(self):
        return reverse('index')


class TaskDeleteView(DeleteView):
    template_name = 'task/task_delete.html'
    model = Task
    pk_url_kwarg = 'pk'
    context_object_name = 'task'
    confirm_delete = False
    redirect_url = 'index'