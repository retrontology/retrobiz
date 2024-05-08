from django.db import models

PAYMENT_CHOICES = [
    ("VENMO", "Venmo"),
    ("PAYPAL", "PayPal"),
    ("ZELLE", "Zelle"),
    ("CHECK", "Check"),
]

class Client(models.Model):
    name = models.CharField(
        max_length=64,
        blank=False,
        null=False,
    )
    address_line1 = models.CharField(
        max_length=64,
        blank=False,
        null=False,
    )
    address_line2 = models.CharField(
        max_length=64,
        blank=True,
        null=False,
    )
    person_of_contact = models.CharField(
        max_length=64,
        blank=True,
        null=False,
    )
    phone = models.CharField(
        max_length=24,
        blank=True,
    )
    email = models.EmailField(
        blank=True
    )

    def __str__(self):
        return self.name

class Payment(models.Model):
    amount = models.IntegerField(
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
    payment = models.ForeignKey(
        to=Payment,
        blank=True,
        null=True,
        on_delete=models.RESTRICT,
    )