from django.contrib import admin
from .models import Tasks

# Register your models here.
@admin.register(Tasks)
class taskAdmin(admin.ModelAdmin):
    list_display = ['task_name','task_description','date_of_task']