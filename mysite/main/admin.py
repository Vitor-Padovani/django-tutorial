from django.contrib import admin
from .models import ToDoList, Item # added!

# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Item)
