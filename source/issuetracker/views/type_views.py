from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from issuetracker.forms import TypeForm
from issuetracker.models import Type


class TypeIndexView(TemplateView):
    template_name = 'type/type_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = Type.objects.all()
        return context


class TypeCreateView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = TypeForm()
        return render(request, 'type/type_create.html', context={
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            Type.objects.create(
                type=form.cleaned_data['type']
            )
            return redirect('type_index')
        else:
            return render(request, 'type/type_create.html', context={
                'form': form,
            })


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