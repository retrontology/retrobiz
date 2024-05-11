# Generated by Django 4.2.11 on 2024-05-11 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateField(null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='client.client')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=128)),
                ('hours', models.SmallIntegerField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=16)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='invoice.invoice')),
            ],
        ),
    ]
