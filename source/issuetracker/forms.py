from django import forms

from issuetracker.models import Status, Type, Task


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


class TypeForm(forms.Form):
    type = forms.CharField(max_length=50)


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status']
        help_texts = {
            'status': 'Please fill out.'
        }