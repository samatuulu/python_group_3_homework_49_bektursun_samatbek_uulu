from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView, View


class DetailView(TemplateView):
    context_key = 'objects'
    model = None
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get(self.pk_url_kwarg)
        context[self.context_key] = get_object_or_404(self.model, pk=pk)
        return context


class UpdateView(View):
    form_class = None
    template_name = None
    redirect_url = ''
    model = None
    pk_url_kwarg = 'pk'
    context_object_name = None

    def get(self, request, *args, **kwargs):
        self.object = self.model.objects.get(id=kwargs['pk'])
        form = self.form_class(instance=self.object)
        context = {'form': form, self.context_object_name: self.object}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.object = self.model.objects.get(id=kwargs['pk'])
        form = self.form_class(instance=self.object, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_redirect_url(self):
        return self.redirect_url

    def form_valid(self, form):
        form.save()
        return redirect(self.get_redirect_url())

    def form_invalid(self, form):
        return render(self.request, self.template_name, context={'form': form})


class DeleteView(View):
    template_name = None
    redirect_url = None
    model = None
    pk_url_kwarg = 'pk'
    context_object_name = 'object'
    confirm_delete = False

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if self.confirm_delete:
            return render(request, self.template_name, context={self.context_object_name: obj})
        else:
            obj.delete()
            return redirect(self.get_redirect_url())

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.redirect_url)

    def get_object(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = get_object_or_404(self.model, pk=pk)
        return obj

    def get_redirect_url(self):
        return self.redirect_url