# Generated by Django 3.1.7 on 2021-03-14 12:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='name')),
                ('chort_code', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='arvr')),
            ],
        ),
    ]