# Generated by Django 4.2.11 on 2024-05-08 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('address_line1', models.CharField(max_length=64)),
                ('address_line2', models.CharField(blank=True, max_length=64)),
                ('person_of_contact', models.CharField(blank=True, max_length=64)),
                ('phone', models.CharField(blank=True, max_length=24)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('total', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateField(null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='invoice.client')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('transaction_id', models.CharField(max_length=128)),
                ('service', models.CharField(choices=[('VENMO', 'Venmo'), ('PAYPAL', 'PayPal'), ('ZELLE', 'Zelle'), ('CHECK', 'Check')], max_length=128)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='invoice.invoice')),
            ],
        ),
    ]
