"""
The basic account infrastructure.

"""

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Table(models.Model):
    number = models.IntegerField()
