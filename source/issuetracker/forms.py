from django import forms
from django.forms import widgets

from issuetracker.models import Status, Type


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=50, label='Summary')
    description = forms.CharField(max_length=2000, required=False, label='Description', widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Status')
    type = forms.ModelChoiceField(queryset=Type.objects.all(), label='Type')


class TypeForm(forms.Form):
    type = forms.CharField(max_length=50)


class StatusForm(forms.Form):
    status = forms.CharField(max_length=50)