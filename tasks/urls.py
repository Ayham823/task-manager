from django.urls import path
from .views import (
    home_view,
    register_view,
    task_list,
    add_task,
    edit_task,
    delete_task,
    toggle_task_status,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/add/', add_task, name='add_task'),
    path('tasks/<int:pk>/edit/', edit_task, name='edit_task'),
    path('tasks/<int:pk>/delete/', delete_task, name='delete_task'),
    path('tasks/<int:pk>/toggle/', toggle_task_status, name='toggle_task_status'),
]