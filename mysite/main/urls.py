# CREATED
# path("<int:id>") looks for num in url and stores in id

from django.urls import path
from . import views

# secondary urls
urlpatterns = [
    path("<int:num>", views.index, name="index"),
]
