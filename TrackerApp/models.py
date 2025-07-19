from django.contrib.auth.models import User
from django.db import models
from django.forms import CharField

#Deadline = Термін виконання (дата)
class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ]

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="todo")
    priority = models.CharField(max_length=60, choices=PRIORITY_CHOICES, default="medium")
    deadline = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    media = models.FileField(upload_to="comments")
    comment = models.CharField(max_length=60)


    def __str__(self):
        return f"Comment by {self.author} on {self.task}"

# Create your models here.
