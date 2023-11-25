from datetime import datetime

from django.db import models
from django.utils import timezone


class Customer(models.Model):
    name = models.CharField(max_length=255)
    Time = models.DateTimeField()
    is_utc = models.BooleanField()
    is_pst = models.BooleanField()
