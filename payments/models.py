from __future__ import unicode_literals
from django.db import models
from accounts.models import Profile


class Payment(models.Model):
    transaction_id = models.CharField(max_length=128)
    phoneNumber = models.CharField(max_length=13)
    regNo = models.ForeignKey(Profile)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=32)
    transaction_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Payments Received"

    def __unicode__(self):
        return self.phoneNumber


