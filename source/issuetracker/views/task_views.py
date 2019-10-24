from urllib.parse import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from issuetracker.forms import TaskForm, SimpleSearchForm
from issuetracker.models import Task


class IndexView(ListView):
    template_name = 'task/index.html'
    context_object_name = 'tasks'
    model = Task
    paginate_by = 2
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form

        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'task/task_create.html'
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('issuetracker:index')


class TaskView(DetailView):
    template_name = 'task/task_detail.html'
    context_key = 'task'
    model = Task
    key_kwarg = 'task.pk'


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task/task_update.html'
    form_class = TaskForm
    context_key = 'task'

    def get_success_url(self):
        return reverse('issuetracker:index')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'task/task_delete.html'
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('issuetracker:index')

