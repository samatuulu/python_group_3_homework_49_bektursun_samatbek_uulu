from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView

from issuetracker.forms import TypeForm
from issuetracker.models import Type


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


class TypeUpdateView(TemplateView):
    def get(self, request, *args, **kwargs):
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        form = TypeForm(data={
            'type': type.type,
        })
        return render(request, 'type/type_update.html', context={
            'form': form,
            'type': type
        })

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        if form.is_valid():
            type.type = form.cleaned_data['type']
            type.save()

            return redirect('type_index')
        else:
            return render(request, 'type/type_update.html', context={
                'form': form,
                'type': type,
            })


class TypeDeleteView(TemplateView):
    def post(self, *args, **kwargs):
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        try:
            type.delete()
            return redirect('type_index')
        except ProtectedError:
            return redirect('type_index')