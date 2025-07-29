from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaulttags import comment

from .forms import TaskForm, CommentForm, UserRegistrationForm
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

@login_required
def profile_view(request):
    tasks = Task.objects.filter(author=request.user)
    comments = Comment.objects.filter(author=request.user)
    tasks_completed = tasks.filter(status="Готово").count()
    return render(request, "home.html", {
        "tasks": tasks,
        "comments": comments,
        "tasks_completed": tasks_completed
    })

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


# Create your views here.

#def TaskListView(request):
    #model = Task
    #template_name = 'tasks/task_list.html'
    #context_object_name = 'tasks'
    #tasks = Task.objects.all()

    #def get_queryset(self):
        #queryset = Task.objects.all()

        #type_filter = self.request.GET.get('type')
        #status_filter = self.request.GET.get('status')
        #priority_filter = self.request.GET.get('priority')
        #price_min = self.request.GET.get('price_min')
        #price_max = self.request.GET.get('price_max')

        #if type_filter:
            #queryset = queryset.filter(type=type_filter)
        #if status_filter:
            #queryset = queryset.filter(status=status_filter)
        #if priority_filter:
            #queryset = queryset.filter(priority=priority_filter)
        #if price_min:
           #queryset = queryset.filter(price__gte=price_min)
        #if price_max:
            #queryset = queryset.filter(price__lte=price_max)

        #return queryset

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['TYPE_TASK'] = Task.TYPE_TASK
        #context['STATUS_CHOICES'] = Task.STATUS_CHOICES
        #context['PRIORITY_CHOICES'] = Task.PRIORITY_CHOICES
        #return context

    #return render(request, 'tasks/task_list.html', {'tasks': tasks})
