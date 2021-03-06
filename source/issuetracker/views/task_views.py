from urllib.parse import urlencode
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from issuetracker.forms import TaskForm, SimpleSearchForm
from issuetracker.models import Task, Project
from issuetracker.views.base_view import UserCheck


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
            context['query']= urlencode({'search': self.search_value})
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


class TaskCreateView(UserCheck, CreateView):

    template_name = 'task/task_create.html'
    model = Task
    form_class = TaskForm

    def get_form(self, **kwargs):
        form = super().get_form()
        pk = self.kwargs.get('pk')
        project = Project.objects.get(pk=pk)

        form.fields['project'].initial = project
        form.fields['created_by'].initial = self.request.user
        return form

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # kwargs['user'] = self.request.user
        kwargs['projects'] = Project.objects.filter(team_project__user=self.request.user,
                                                    team_project__finished_at=None).values('pk')
        print(kwargs)
        return kwargs

    def form_valid(self, form):
        project_pk = self.request.POST.get('project')
        checker = self.checker(project_pk, self.request.user)
        if checker:
            return super().form_valid(form)
        return render(self.request, 'task/error_user.html')

    def get_success_url(self):
        return reverse('issuetracker:index')


class TaskView(DetailView):
    template_name = 'task/task_detail.html'
    context_key = 'task'
    model = Task
    key_kwarg = 'task.pk'


class TaskUpdateView(UserCheck, UpdateView):
    model = Task
    template_name = 'task/task_update.html'
    form_class = TaskForm
    context_key = 'task'

    def get(self, *args, **kwargs):
        task = self.get_object()
        project_pk = task.project.pk
        checker = self.checker(project_pk, self.request.user)
        print('here')
        if checker:
            return super().get(self.request, *args, **kwargs)
        return render(self.request, 'task/error_user.html')

    def form_valid(self, form):
        project_pk = self.request.POST.get('project')
        checker = self.checker(project_pk, self.request.user)
        if checker:
            return super().form_valid(form)
        return render(self.request, 'task/error_user.html')

    def get_success_url(self):
        return reverse('issuetracker:index')


class TaskDeleteView(UserCheck, DeleteView):
    template_name = 'task/task_delete.html'
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('issuetracker:index')

    def get(self, *args, **kwargs):
        task = self.get_object()
        project_pk = task.project.pk
        checker = self.checker(project_pk, self.request.user)
        if checker:
            return super().get(self.request, *args, **kwargs)
        return render(self.request, 'task/error_user.html')