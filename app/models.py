from enum import unique
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Company(models.Model):
    cmp_name=models.TextField()
    cmp_shortname=models.CharField(max_length=8,validators=[MinLengthValidator(3)])
    cmp_location=models.TextField()
    cmp_weburl=models.TextField()

    class Meta:
        verbose_name_plural="Company"

class User(models.Model):
    username=models.CharField(max_length=20,validators=[MinLengthValidator(5)])
    email=models.CharField(max_length=30,validators=[MinLengthValidator(15)])
    password=models.CharField(max_length=15,validators=[MinLengthValidator(8)])
    status=models.CharField(max_length=1,validators=[MinLengthValidator(1)])
    class Meta:
        unique_together=("username","email")

class Department(models.Model):
    dept_name=models.CharField("name",max_length=255,validators=[MinLengthValidator(10)])
    chort_code=models.CharField("arvr",max_length=10,validators=[MinLengthValidator(2)])



