from django.urls import path
from issuetracker.views import IndexView, TaskView, TaskCreateView, TaskUpdateView, TaskDeleteView, TypeIndexView, \
    TypeCreateView, TypeUpdateView, TypeDeleteView, StatusIndexView, StatusCreateView, StatusUpdateView, \
    StatusDeleteView, ProjectIndexView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_detail'),
    path('task/add/', TaskCreateView.as_view(), name='task_add'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('type/', TypeIndexView.as_view(), name='type_index'),
    path('type/add/', TypeCreateView.as_view(), name='type_add'),
    path('type/<int:pk>/update/', TypeUpdateView.as_view(), name='type_update'),
    path('type/<int:pk>/delete/', TypeDeleteView.as_view(), name='type_delete'),
    path('status/', StatusIndexView.as_view(), name='status_index'),
    path('status/add/', StatusCreateView.as_view(), name='status_add'),
    path('status/<int:pk>/update/', StatusUpdateView.as_view(), name='status_update'),
    path('status/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
    path('project/', ProjectIndexView.as_view(), name='project_index'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),

]

app_name = 'issuetracker'