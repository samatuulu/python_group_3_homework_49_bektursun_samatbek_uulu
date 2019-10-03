from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from issuetracker.forms import StatusForm
from issuetracker.models import Status


class StatusIndexView(TemplateView):
    template_name = 'status/status_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status'] = Status.objects.all()
        return context


class StatusCreateView(TemplateView):
    template_name = 'status/status_create.html'

    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'status/status_create.html', context={
                'form': form
            })

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            Status.objects.create(
                status=form.cleaned_data['status']
            )
            return redirect('status_index')
        else:
            return render(request, 'status/status_create.html', context={
                'form': form
            })


class StatusUpdateView(TemplateView):
    template_name = 'status/status_update.html'

    def get(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        form = StatusForm(data={
            'status': status.status
        })
        return render(request, 'status/status_update.html', context={
            'form': form,
            'status': status
        })

    def post(self,request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        if form.is_valid():
            status.status = form.cleaned_data['status']
            status.save()

            return redirect('status_index')
        else:
            return render(request, 'status/status_update.html', context={
                'form': form,
                'status': status
            })


class StatusDeleteView(TemplateView):
    def post(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        try:
            status.delete()
            return redirect('status_index')
        except ProtectedError:
            return redirect('status_index')
