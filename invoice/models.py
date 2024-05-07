from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=32)
    middle_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

class Client(models.Model):
    name = models.CharField(max_length=200)
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200)
    point_of_contact = models.ForeignKey(
        to=Contact,
        on_delete=models.PROTECT,
    )

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
        on_delete=models.PROTECT,
    )
    pub_date = models.DateTimeField("date published")