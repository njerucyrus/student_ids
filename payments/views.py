from django.shortcuts import render


def initiate_payment(request):
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
