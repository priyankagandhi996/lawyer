# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.
class City(models.Model):
    cityname=models.CharField(max_length=50)

    def __str__(self):
        return self.cityname

class Issues(models.Model):
    issuesname=models.CharField(max_length=50)

    def __str__(self):
        return self.issuesname

class Lawyer(models.Model):
    user=models.OneToOneField(User ,on_delete=models.CASCADE , related_name='users' ,null=True)
    city=models.ForeignKey(City ,on_delete=models.CASCADE ,null=True)
    issues=models.ManyToManyField(Issues)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13 ,default="9999999999")


class Customer(models.Model):
    user=models.OneToOneField(User ,on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13 ,default="9999999999")
