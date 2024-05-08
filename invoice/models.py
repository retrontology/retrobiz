from django.db import models
from client.models import Client

class Invoice(models.Model):
    number = models.AutoField(
        primary_key=True,
        blank=False,
        null=False,
        unique=True,
    )
    total = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    client = models.ForeignKey(
        to=Client,
        blank=False,
        null=False,
        on_delete=models.RESTRICT,
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )
    due_date = models.DateField(
        null=True
    )
