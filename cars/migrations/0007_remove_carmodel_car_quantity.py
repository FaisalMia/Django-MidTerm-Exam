# Generated by Django 5.0.7 on 2024-09-08 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_carmodel_car_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='car_quantity',
        ),
    ]