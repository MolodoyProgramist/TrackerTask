from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import DateInput
from .models import  Task, Comment


# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'author', 'status', 'priority', 'deadline', 'created']
#
# class CommentForm(forms.ModelForm):
    #class Meta:
        #model = Comment
        #fields = ['text','data','author','task', 'media', 'comment']


















