from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Category, Tag, Task, Subtask

admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Task)
admin.site.register(Subtask)