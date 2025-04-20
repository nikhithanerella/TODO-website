from django.contrib import admin
from home.models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('tasktitle', 'taskdesc', 'user')  # Add 'user' here to display it in the list view

admin.site.register(Task, TaskAdmin)

