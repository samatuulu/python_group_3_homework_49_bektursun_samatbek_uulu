from django.contrib.auth.models import User
from django.db import models

STATUS_CHOICE = 'Active'
STATUS_CHOICE_2 = 'Locked'

STATUS_CATEGORY = (
    (STATUS_CHOICE, 'Active'),
    (STATUS_CHOICE_2, 'Locked')
)


def get_admin():
    return User.objects.get(username='admin').id


class Task(models.Model):
    summary = models.CharField(max_length=50, null=False, blank=False, verbose_name='Summary')
    description = models.TextField(max_length=2000, null=True, blank=True)
    status = models.ForeignKey('issuetracker.Status', related_name='task_status', on_delete=models.PROTECT, verbose_name='Status')
    type = models.ForeignKey('issuetracker.Type', related_name='task_type', on_delete=models.PROTECT, verbose_name='Type')
    project = models.ForeignKey('issuetracker.Project', related_name='task_project', on_delete=models.PROTECT, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    created_by = models.ForeignKey(User, related_name='created', null=False, blank=False, default=get_admin, on_delete=models.PROTECT, verbose_name='Created by')
    assigned_to = models.ForeignKey(User, related_name='assigned', on_delete=models.PROTECT, verbose_name='Assigned to')

    def __str__(self):
        return self.summary


class Type(models.Model):
    type = models.CharField(max_length=50, verbose_name='Type')

    def __str__(self):
        return self.type


class Status(models.Model):
    status = models.CharField(max_length=50, verbose_name='Status')

    def __str__(self):
        return self.status


class Project(models.Model):
    tittle = models.CharField(max_length=50, null=False, blank=False, verbose_name='Title')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    status = models.CharField(max_length=25, verbose_name='Project status', choices=STATUS_CATEGORY, default=STATUS_CHOICE)

    def __str__(self):
        return self.tittle


class Team(models.Model):
    user = models.ForeignKey(User, related_name='team_user', verbose_name='Users in team', on_delete=models.PROTECT)
    project_key = models.ForeignKey(Project, related_name='team_project', verbose_name='Projects', on_delete=models.PROTECT)
    created_at = models.DateField(verbose_name='Started at')
    finished_at = models.DateField(verbose_name='Finished at', null=True, blank=True)