from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.
def index(response, num):
    ls = ToDoList.objects.get(id=num)
    item = ls.item_set.get(id=1)
    return HttpResponse(f"<h1>Olá, Mundo!</h1>{ls.name}<p>{item.text}</p>")

    