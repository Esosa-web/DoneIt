from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # AbstractUser already includes username, email, password, and date_joined
    pass

class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=7)  # Hex color code

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='To Do')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    description = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Subtask for {self.task.title}"