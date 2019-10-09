from django import forms

from issuetracker.models import Status, Type, Task, Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['created_at']
        help_texts = {
            'summary': 'A little words about the task',
            'description': 'Give more information about the task (optional)'
        }
        error_messages = {
            'summary': {
                'required': 'This field needs to be fill out!'
            }
        }


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['type']
        help_texts = {
            'type': 'Please fill out this field'
        }


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status']
        help_texts = {
            'status': 'Please fill out.'
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['tittle', 'description']