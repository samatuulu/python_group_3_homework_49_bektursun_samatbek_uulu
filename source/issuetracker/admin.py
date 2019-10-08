from django.contrib import admin
from .models import Task, Type, Status, Project


class TaskAdmin(admin.ModelAdmin):
    list_display = ['pk', 'summary', 'description', 'status', 'type', 'created_at']
    list_filter = ['summary']
    list_display_links = ['pk', 'summary']
    search_fields = ['summary', 'description']
    fields = ['summary', 'description', 'status', 'type', 'project', 'created_at']
    readonly_fields = ['created_at']


admin.site.register(Task, TaskAdmin)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Project)
