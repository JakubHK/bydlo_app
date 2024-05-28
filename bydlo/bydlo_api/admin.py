from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'deadline')

admin.site.register(Task,TaskAdmin)
    