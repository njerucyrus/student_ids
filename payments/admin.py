from django.contrib import admin
from payments.models import Payment, StudentIdFee


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


class StudentIdFeeAdmin(admin.ModelAdmin):
    list_display = ['academic_year', 'id_fee']

    class Meta:
        model = StudentIdFee
admin.site.register(StudentIdFee, StudentIdFeeAdmin)

