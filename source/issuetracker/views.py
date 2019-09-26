from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from issuetracker.forms import TaskForm, TypeForm, StatusForm
from issuetracker.models import Task, Type, Status


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskView(TemplateView):
    template_name = 'task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task_pk = kwargs.get('pk')
        context['task'] = get_object_or_404(Task, pk=task_pk)
        return context


class TaskCreateView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'task_create.html', context={
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            Task.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                type=form.cleaned_data['type']
            )
            return redirect('index')
        else:
            return render(request, 'task_create.html', context={
                'form': form
            })


class TaskUpdateView(TemplateView):
    def get(self, request, *args, **kwargs):
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        form = TaskForm(data={
            'summary': task.summary,
            'description': task.description,
            'status': task.status,
            'type': task.type
        })
        return render(request, 'task_update.html', context={
            'form': form,
            'task': task
        })

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        if form.is_valid():
            task.summary = form.cleaned_data['summary']
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.type = form.cleaned_data['type']
            task.save()

            return redirect('task_detail', pk=task_pk)
        else:
            return render(request, 'task_update.html', context={
                'form': form,
                'task': task,
            })


class TaskDeleteView(TemplateView):
    def post(self, *args, **kwargs):
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        task.delete()
        return redirect('index')


class TypeIndexView(TemplateView):
    template_name = 'type_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = Type.objects.all()
        return context


class TypeCreateView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = TypeForm()
        return render(request, 'type_create.html', context={
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
            return render(request, 'type_create.html', context={
                'form': form,
            })


class TypeUpdateView(TemplateView):
    def get(self, request, *args, **kwargs):
        type_pk = kwargs.get('pk')
        type = get_object_or_404(Type, pk=type_pk)
        form = TypeForm(data={
            'type': type.type,
        })
        return render(request, 'type_update.html', context={
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
            return render(request, 'type_update.html', context={
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


class StatusIndexView(TemplateView):
    template_name = 'status_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status'] = Status.objects.all()
        return context


class StatusCreateView(TemplateView):
    template_name = 'status_create.html'

    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'status_create.html', context={
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
            return render(request, 'status_create.html', context={
                'form': form
            })


class StatusUpdateView(TemplateView):
    template_name = 'status_update.html'

    def get(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = get_object_or_404(Status, pk=status_pk)
        form = StatusForm(data={
            'status': status.status
        })
        return render(request, 'status_update.html', context={
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
            return render(request, 'status_update.html', context={
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
