from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView

from issuetracker.forms import TaskForm
from issuetracker.models import Task
from .base_view import DetailView


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


class TaskUpdateView(TemplateView):
    def get(self, request, *args, **kwargs):
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        form = TaskForm(data={
            'summary': task.summary,
            'description': task.description,
            'status': task.status,
            'type': task.type
        })
        return render(request, 'task/task_update.html', context={
            'form': form,
            'task': task
        })

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        if form.is_valid():
            task.summary = form.cleaned_data['summary']
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.type = form.cleaned_data['type']
            task.save()

            return redirect('task_detail', pk=task_pk)
        else:
            return render(request, 'task/task_update.html', context={
                'form': form,
                'task': task,
            })


class TaskDeleteView(TemplateView):
    def post(self, *args, **kwargs):
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        task.delete()
        return redirect('index')