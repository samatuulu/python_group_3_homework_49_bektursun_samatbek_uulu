from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserCreationForm


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
    return render(request, 'login.html', context=context)


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