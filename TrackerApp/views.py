from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaulttags import comment

from .forms import TaskForm, CommentForm
# from .forms import TaskForm, CommentForm
from .models import  Task, Comment


def TaskCreateView(request):
     if request.method == 'POST':
         form = TaskForm(request.POST)
         if form.is_valid():
             task = form.save(commit=False)
             if request.user.is_authenticated:
                 task.autor = request.user  # Прив’язуємо автора
             task.save()
             return redirect('task-list')  # Заміни на свій URL або ім’я маршруту
     else:
         form = TaskForm()
     return render(request, 'tasks/task_form.html', {'form': form})

def CommentView(request, task_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                comment.user = request.user
            comment.task = get_object_or_404(Task, id=task_id)
            comment.save()
            return redirect('task-detail', pk=task_id)
    else:
        form = CommentForm()

    # Если GET — редирект на detail задачи, либо можно отобразить форму
    return redirect('task-detail', pk=task_id)

def TaskListView(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def TaskDetailView(request, pk):
    task = get_object_or_404(Task, pk=pk)
    comments = Comment.objects.filter(task=task).order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                comment.user = request.user
            comment.task = task
            comment.save()
            return redirect('task-detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'tasks/task_detail.html', {
        'task': task,
        'comments': comments,
        'form': form,
    })


# Create your views here.
