from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'date', 'complete')
    list_filter = ('complete', 'date')
    search_fields = ('content',)
