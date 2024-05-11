from django.db import models
from client.models import Client

class Invoice(models.Model):
    number = models.AutoField(
        primary_key=True,
        blank=False,
        null=False,
        unique=True,
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

class Item(models.Model):
    invoice = models.ForeignKey(
        to=Invoice,
        blank=False,
        null=False,
        on_delete=models.RESTRICT,
    )
    description = models.CharField(
        max_length=128,
        blank=False,
        null=False,
    )
    hours = models.SmallIntegerField()
    rate = models.DecimalField(
        max_digits=16,
        decimal_places=2,
        blank=False,
        null=False,
    )