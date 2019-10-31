from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, ListView

from .forms import UserCreationForm, UserUpdatePasswordForm, UserForm, ProfileForm


def login_view(request):
    context = {}
    page_name = request.GET.get('next')
    get_to_other_page = request.session.setdefault('get_to_other_page', page_name)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(get_to_other_page)
        else:
            context['has_error'] = True
    return render(request, 'registration/login.html', context=context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('issuetracker:index')


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('issuetracker:index')
    else:
        form = UserCreationForm()

    return render(request, 'user_create.html', context={'form': form})


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'


class UserUpdateView(UserPassesTestMixin,  UpdateView):
    model = User
    template_name = 'user_update.html'
    context_object_name = 'user_obj'

    def test_func(self):
        return self.get_object() == self.request.user

    @transaction.atomic()
    def post(self, request, *args, **kwargs):
        user_form = UserForm(instance=request.user, data=request.POST)
        profile_form = ProfileForm(instance=request.user.user_link, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('issuetracker:index')
        else:
            return render(request, 'user_update.html', {
                'user_form': user_form,
                'profile_form': profile_form
            })

    def get(self, request, *args, **kwargs):
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.user_link)

        return render(request, 'user_update.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })

    def get_success_url(self):
        return reverse('accounts:user_detail', kwargs={'pk': self.object.pk})


# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.user_link)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             # messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('accounts:all_users')
#
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.user_link)
#     return render(request, 'user_update.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })


class UserUpdatePasswordView(UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user_change_password.html'
    form_class = UserUpdatePasswordForm
    context_object_name = 'user_obj'

    def test_func(self):
        return self.get_object() == self.request.user

    def get_success_url(self):
        return reverse('accounts:login')


class AllUsersView(ListView):
    template_name = 'all_users.html'
    context_object_name = 'user_obj'
    model = User