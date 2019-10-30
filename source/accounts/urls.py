from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import login_view, logout_view, register_view, UserDetailView, UserUpdateView, \
    UserUpdatePasswordView, AllUsersView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', register_view, name='create'),
    path('profile/<pk>/', UserDetailView.as_view(), name='user_detail'),
    path('profile/<pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('profile/<pk>/update-password/', UserUpdatePasswordView.as_view(), name='user_change_password'),
    path('users/', AllUsersView.as_view(), name='all_users')

]

app_name = 'accounts'