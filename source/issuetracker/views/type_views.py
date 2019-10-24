from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from issuetracker.forms import TypeForm
from issuetracker.models import Type


class TypeIndexView(ListView):
    template_name = 'type/type_index.html'
    context_object_name = 'type'

    def get_queryset(self):
        return Type.objects.all()


class TypeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'type/type_create.html'
    model = Type
    form_class = TypeForm

    def get_success_url(self):
        return reverse('issuetracker:type_index')


class TypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Type
    template_name = 'type/type_update.html'
    form_class = TypeForm
    context_object_name = 'type'

    def get_success_url(self):
        return reverse('issuetracker:type_index')


class TypeDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'type/type_delete.html'
    model = Type
    context_object_name = 'type'
    success_url = reverse_lazy('issuetracker:type_index')