"""
URL configuration for TrackerProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from TrackerApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', views.TaskListView, name='task-list'),
    path('tasks/create/', views.TaskCreateView, name='task-create'),
    path('tasks/<int:pk>/', views.TaskDetailView, name='task-detail'),
    path('tasks/<int:task_id>/comment/', views.CommentView, name='task-comment'),
    path('tasks/edit/', views.task_edit_selection, name='task-edit-select'),
    path('tasks/<int:pk>/edit/', views.task_edit_view, name='task-edit'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.profile_view, name='home'),

    # Либо на home, либо на login, но не оба
    path('', lambda request: redirect('home/', permanent=False)),

    # Добавляем include в конце, если нужно
    path('', include("auth_system.urls")),
]
#<th class="text-center">Дії</th>
#<a href="{% url 'task-create' %}" class="btn btn-primary mb-3">Створити завдання</a>