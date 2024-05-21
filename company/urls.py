from django.urls import path
from . import views

app_name = "company"
urlpatterns = [
    path("", views.index, name="index"),
    path("edit", views.edit, name="edit"),
    path("save", views.save, name="save"),
]
