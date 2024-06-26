# Generated by Django 4.2.13 on 2024-05-21 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('address_line1', models.CharField(max_length=64)),
                ('address_line2', models.CharField(blank=True, max_length=64)),
                ('owner', models.CharField(blank=True, max_length=64)),
                ('phone', models.CharField(blank=True, max_length=24)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
