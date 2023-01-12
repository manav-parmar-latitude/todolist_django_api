from django.contrib import admin
from .models import TodoList

@admin.register(TodoList)
class Todolist(admin.ModelAdmin):
    list_display=['id','username','name','description','date_created','completed']


