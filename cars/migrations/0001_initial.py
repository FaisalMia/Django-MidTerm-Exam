# Generated by Django 5.0.7 on 2024-09-07 05:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('car_name', models.CharField(max_length=200)),
                ('car_price', models.IntegerField()),
                ('car_brand_name', models.CharField(max_length=250)),
                ('CarBrand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='cars.carbrand')),
            ],
        ),
    ]
