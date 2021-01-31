from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """User model"""
    job = models.CharField(max_length=428)
    domain_name = models.CharField(max_length=128)
    phone_number = models.IntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=428)
    text = models.TextField(max_length=1024)
    integer = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=1024)
    date = models.DateField(blank=True, null=True)
