from urllib.parse import urlencode

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.views.generic.base import View

from issuetracker.forms import ProjectForm, SimpleSearchForm, MemberForm
from issuetracker.models import Project, Team
from _datetime import datetime


class ProjectIndexView(ListView):
    template_name = 'project/project_index.html'
    context_object_name = 'project'
    model = Project

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list = object_list, **kwargs)
        context['form'] = self.form

        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(tittle__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


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


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'project/project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('issuetracker:project_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        users = form.cleaned_data.pop('user_member')
        current_user = self.request.user
        users_list = list(users)
        users_list.append(current_user)
        self.object = form.save()
        for user in users_list:
            Team.objects.create(user=user, project_key=self.object, created_at=datetime.now())
        return redirect(self.get_success_url())


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'project/project_update.html'
    model = Project
    context_object_name = 'project'
    form_class = ProjectForm

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class=None)
    #     form.fields.pop('user_member')
    #     return form



    # def form_valid(self, form):
    #     users = form.cleaned_data.pop('user_member')
    #     current_user = self.request.user
    #     users_list = list(users)
    #     users_list.append(current_user)
    #     self.object = form.save()
    #     for user in users_list:
    #         Team.objects.create(user=user, project_key=self.object, created_at=datetime.now())
    #     return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('issuetracker:project_detail', kwargs={'pk': self.object.pk})


class UpdateProjectMember(LoginRequiredMixin, UpdateView):
    template_name = 'team/update_member.html'
    context_object_name = 'project'
    form_class = MemberForm
    model = Project

    def form_valid(self, form):
        user = self.get_user()
        self.project = self.get_project()
        Team.objects.create(user=user, project_key=self.project)
        return self.get_success_url()

    def get_project(self):
        project_pk = self.kwargs['pk']
        return Project.objects.get(pk=project_pk)

    def get_user(self):
        user_pk = self.request.POST['user_member']
        return User.objects.get(pk=user_pk)

    def get_success_url(self):
        return redirect('issuetracker:project_index')


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'project/project_delete.html'
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('issuetracker:project_index')