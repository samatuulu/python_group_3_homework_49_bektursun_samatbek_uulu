from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from issuetracker.forms import StatusForm
from issuetracker.models import Status


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
        return reverse('issuetracker:status_index')


class StatusUpdateView(UpdateView):
    template_name = 'status/status_update.html'
    model = Status
    form_class = StatusForm
    context_object_name = 'status'

    def get_success_url(self):
        return reverse('issuetracker:status_index')


class StatusDeleteView(DeleteView):
    template_name = 'status/status_delete.html'
    model = Status
    context_object_name = 'status'
    success_url = reverse_lazy('issuetracker:status_index')