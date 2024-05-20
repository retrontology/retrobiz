from django.db import models
from invoice.models import Invoice

PAYMENT_CHOICES = [
    ("VENMO", "Venmo"),
    ("PAYPAL", "PayPal"),
    ("ZELLE", "Zelle"),
    ("CHECK", "Check"),
]

class Payment(models.Model):
    amount = models.DecimalField(
        max_digits=16,
        decimal_places=2,
        blank=False,
        null=False,
    )
    transaction_id = models.CharField(
        blank=False,
        null=False,
        max_length=128,
    )
    service = models.CharField(
        choices=PAYMENT_CHOICES,
        blank=False,
        null=False,
        max_length=128,
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False,
    )
    invoice = models.ForeignKey(
        to=Invoice,
        blank=True,
        null=True,
        on_delete=models.RESTRICT,
    )