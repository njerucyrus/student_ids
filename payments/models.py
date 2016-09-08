from __future__ import unicode_literals
from django.db import models


class StudentIdFee(models.Model):
    academic_year = models.CharField(max_length=20, unique=True, null=True)
    id_fee = models.DecimalField("ID Fee (Ksh)", max_digits=10, decimal_places=2)

    def __unicode__(self):
        return str(self.id_fee)


class Payment(models.Model):
    transaction_id = models.CharField(max_length=128)
    phoneNumber = models.CharField(max_length=13)
    regNo = models.CharField(max_length=32, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=32)
    transaction_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Payments Received"

    def __unicode__(self):
        return self.phoneNumber


