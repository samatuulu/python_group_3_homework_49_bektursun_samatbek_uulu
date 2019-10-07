from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView

from issuetracker.forms import StatusForm
from issuetracker.models import Status
from issuetracker.views.base_view import UpdateView


class StatusIndexView(ListView):
    template_name = 'status/status_index.html'
    context_object_name = 'status'

    def get_queryset(self):
        return Status.objects.all()


class StatusCreateView(CreateView):
    template_name = 'status/status_create.html'
    model = Status
    form_class = StatusForm

    def get_success_url(self):
        return reverse('status_index')


class StatusUpdateView(UpdateView):
    template_name = 'status/status_update.html'
    model = Status
    form_class = StatusForm
    context_object_name = 'status'

    def get_redirect_url(self):
        return reverse('status_index')


class StatusDeleteView(TemplateView):
    def post(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        try:
            status.delete()
            return redirect('status_index')
        except ProtectedError:
            return redirect('status_index')
