from django.urls import reverse
from django.views.generic import ListView, CreateView

from issuetracker.forms import TypeForm
from issuetracker.models import Type
from issuetracker.views.base_view import UpdateView, DeleteView


class TypeIndexView(ListView):
    template_name = 'type/type_index.html'
    context_object_name = 'type'

    def get_queryset(self):
        return Type.objects.all()


class TypeCreateView(CreateView):
    template_name = 'type/type_create.html'
    model = Type
    form_class = TypeForm

    def get_success_url(self):
        return reverse('type_index')


class TypeUpdateView(UpdateView):
    template_name = 'type/type_update.html'
    model = Type
    form_class = TypeForm
    context_object_name = 'type'

    def get_redirect_url(self):
        return reverse('type_index')


class TypeDeleteView(DeleteView):
    template_name = 'type/type_delete.html'
    model = Type
    pk_url_kwarg = 'pk'
    context_object_name = 'type'
    redirect_url = 'type_index'