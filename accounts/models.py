from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class School(models.Model):
    school_name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.school_name


class Department(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.department_name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.course_name


class Profile(models.Model):
    user = models.OneToOneField(User)
    phoneNumber = models.CharField(max_length=13)
    regNo = models.CharField("RegNo", max_length=32, unique=True)
    national_id = models.PositiveIntegerField()
    school = models.ForeignKey(School)
    department = models.ForeignKey(Department)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.regNo


class IdApplication(models.Model):
    user = models.OneToOneField(User)
    passport = models.ImageField("Passport Photo ", upload_to="img/passports")

    APPL_TYPE = (
        ('F', 'First Time'),
        ('R', 'Replacement'),
    )

    application_type = models.CharField(max_length=32, choices=APPL_TYPE, default=APPL_TYPE[0][0])
    paid = models.BooleanField(default=False)
    status = models.CharField(max_length=20, default="Pending")
    date_applied = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.user)


class ContactMessage(models.Model):
    phoneNumber = models.CharField(max_length=13)
    message = models.TextField(max_length=200)

    def __unicode__(self):
        return self.phoneNumber



