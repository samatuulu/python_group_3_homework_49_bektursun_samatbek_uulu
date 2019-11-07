from django import forms
from django.contrib.auth.models import User

from issuetracker.models import Status, Type, Task, Project


class TaskForm(forms.ModelForm):
    def __init__(self, **kwargs):
        # self.user = kwargs.pop('user')
        self.projects = kwargs.pop('projects')
        super().__init__(**kwargs)
        self.fields['assigned_to'].queryset = User.objects.filter(team_user__project_key__in=self.projects)

    # assigned_to = forms.CharField(max_length=100, label='Assigned_to', required=False)
    # assigned_to = forms.ModelChoiceField(queryset=User.objects.filter(team__project_key=))

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

    # def save(self, commit=True):
    #     super(TaskForm).save(commit=commit)


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
        fields = ['tittle', 'description', 'status']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Search')