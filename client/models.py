from django.db import models

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