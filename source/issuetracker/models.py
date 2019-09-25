from django.db import models


class Task(models.Model):
    summary = models.CharField(max_length=50, null=False, blank=False, verbose_name='Summary')
    description = models.TextField(max_length=2000, null=True, blank=True)
    status = models.ForeignKey('issuetracker.Status', related_name='task_status', on_delete=models.PROTECT, verbose_name='Status')
    type = models.ForeignKey('issuetracker.Type', related_name='task_type', on_delete=models.PROTECT, verbose_name='Type')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

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