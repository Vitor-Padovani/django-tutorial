# CREATED
# path("<int:id>") looks for num in url and stores in id

from django.urls import path
from . import views

# secondary urls
urlpatterns = [
    path("<int:num>", views.index, name="index"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
]
