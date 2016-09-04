from django.contrib import admin
from payments.models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['transaction_id',
                    'phoneNumber',
                    'regNo',
                    'amount',
                    'status',
                    'transaction_date'
                    ]

    class Meta:
        model = Payment
admin.site.register(Payment, PaymentAdmin)