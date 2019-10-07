from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from issuetracker.forms import TaskForm
from issuetracker.models import Task


class IndexView(ListView):
    template_name = 'task/index.html'
    context_object_name = 'tasks'
    paginate_by = 2
    paginate_orphans = 1

    def get_queryset(self):
        return Task.objects.all().order_by('-created_at')


class TaskCreateView(CreateView):
    template_name = 'task/task_create.html'
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('index')


class TaskView(DetailView):
    template_name = 'task/task_detail.html'
    context_key = 'task'
    model = Task
    key_kwarg = 'task.pk'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task/task_update.html'
    form_class = TaskForm
    context_key = 'task'

    def get_success_url(self):
        return reverse('index')


class TaskDeleteView(DeleteView):
    template_name = 'task/task_delete.html'
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('index')