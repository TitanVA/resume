from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    linkedin = models.CharField(max_length=100, blank=True, null=True)
