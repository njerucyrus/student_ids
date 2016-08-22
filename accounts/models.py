from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    phoneNumber = models.CharField(max_length=13)
    regNo = models.CharField("RegNo", max_length=32, unique=True)
    national_id = models.PositiveIntegerField()
    school = models.CharField(max_length=50)
    department = models.CharField(max_length=50)

    def __unicode__(self):
        return self.regNo


class IdApplication(models.Model):
    user = models.OneToOneField(User)
    regNo = models.CharField(max_length=32)
    full_name = models.CharField(max_length=100)
    passport = models.ImageField(upload_to="img/passports")

    def __unicode__(self):
        return self.regNo

