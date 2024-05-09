from django.urls import path
from . import views

app_name = "payment"
urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("new", views.new, name="new"),
    path("view/<int:payment_id>", views.view, name="view"),
]
