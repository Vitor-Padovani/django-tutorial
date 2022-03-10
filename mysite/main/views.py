from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.
def index(response, num):
    ls = ToDoList.objects.get(id=num)
    return render(response, "main/list.html", {"ls": ls})

def home(response):
    return render(response, "main/home.html")
    