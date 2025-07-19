from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaulttags import comment

# from .forms import TaskForm, CommentForm
from .models import  Task, Comment

# def TaskCreateView(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task = form.save(commit=False)
#             if request.user.is_authenticated:
#                 task.autor = request.user  # Прив’язуємо автора
#             task.save()
#             return redirect('task-list')  # Заміни на свій URL або ім’я маршруту
#     else:
#         form = TaskForm()
#     return render(request, 'tasks/task_form.html', {'form': form})
#
# def TaskListView(request):
#     tasks = Task.objects.all()  # отримуємо всі завдання (пізніше можна фільтрувати)
#     return render(request, 'tasks/task_list.html', {'tasks': tasks})
#
# def CommentView(request, task_id):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             if request.user.is_authenticated:
#                 comment.user = request.user  # прив’язуємо автора коментаря
#             comment.task = get_object_or_404(Task, id=task_id)  # прив’язуємо коментар до завдання
#             comment.save()
#             return redirect('task-detail', pk=task_id)  # перенаправлення на сторінку завдання
#     else:
#         form = CommentForm()
#     # Тут можна повернути форму, якщо GET — але частіше коментарі додають тільки POST-ом
#     return redirect('task-detail', pk=task_id)
#
# def TaskDetailView(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     comments = Comment.objects.filter(task=task).order_by('-created_at')
#
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             if request.user.is_authenticated:
#                 comment.user = request.user
#             comment.task = task
#             comment.save()
#             return redirect('task-detail', pk=pk)
#     else:
#         form = CommentForm()
#
#     return render(request, 'tasks/task_detail.html', {
#         'task': task,
#         'comments': comments,
#         'form': form,
#     })


# Create your views here.
