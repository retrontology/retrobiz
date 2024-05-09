from django.urls import path
from . import views

app_name = "invoice"
urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("new", views.new, name="new"),
    path("view/<int:invoice_number>", views.view, name="view"),
]
