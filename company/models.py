from django.db import models

class Company(models.Model):
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
    owner = models.CharField(
        max_length=64,
        blank=True,
        null=False,
    )
    phone = models.CharField(
        max_length=24,
        blank=True,
        null=False,
    )
    email = models.EmailField(
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name

def get_company() -> Company:
    return Company.objects.first()