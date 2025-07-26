from django.contrib.auth.models import User
from django.db import models
from django.forms import CharField
from django.utils import timezone

#Deadline = Термін виконання (дата)
class Task(models.Model):
    STATUS_CHOICES = [
        ("Not selected", "Не выбрано"),
        ("В ожидании", "В ожидании"),
        ("В прогрессе", "В прогрессе"),
        ("Готово", "Готово"),
    ]

    PRIORITY_CHOICES = [
        ("Not selected", "Не выбрано"),
        ("low", "Низкий"),
        ("medium", "Средний"),
        ("high", "Высокий"),
    ]

    TYPE_TASK = [
        ("Not selected", "Не выбрано"),
        ("Programming", "Программирование"),
        ("Design", "Дизайн"),
        ("Testing", "Тестирование"),
        ("Marketing", "Маркетинг / Реклама"),
        ("Arbitrage", "Арбитраж(Трафика)"),
        ("Editing", "Монтаж / Видеомонтаж"),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=50, choices=TYPE_TASK, default="Not selected")
    price = models.DecimalField(max_digits=9000000, decimal_places=2, default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Не выбрано")
    priority = models.CharField(max_length=60, choices=PRIORITY_CHOICES, default="Не выбрано")
    deadline = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    media = models.FileField(upload_to="comments", null=True, blank=True)
    comment = models.CharField(max_length=60)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"Comment by {self.author} on {self.task}"

# Create your models here.
