# Generated by Django 3.2.3 on 2021-05-17 14:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cleaner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address', models.TextField(null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('hours_worked', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
