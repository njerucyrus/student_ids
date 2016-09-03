from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class School(models.Model):
    school_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.school_name


class Department(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=32)

    def __unicode__(self):
        return self.department_name


class Profile(models.Model):
    user = models.OneToOneField(User)
    phoneNumber = models.CharField(max_length=13)
    regNo = models.CharField("RegNo", max_length=32, unique=True)
    national_id = models.PositiveIntegerField()
    school = models.ForeignKey(School)
    department = models.ForeignKey(Department)

    def __unicode__(self):
        return self.regNo


class IdApplication(models.Model):
    user = models.OneToOneField(User)
    regNo = models.CharField(max_length=32)
    full_name = models.CharField(max_length=100)
    passport = models.ImageField(upload_to="img/passports")
    paid = models.BooleanField(default=False)
    date_applied = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.regNo


