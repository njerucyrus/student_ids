from django.shortcuts import render, HttpResponse
from payments.forms import PaymentForm
from django.contrib.auth.decorators import login_required
from payments.models import Payment, StudentIdFee
from student_ids.settings import  apiKey, username, currencyCode, productName, metadata
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException


@login_required(login_url='/login/')
def make_payment(request):
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            cd = payment_form.cleaned_data
            phoneNumber = cd['phoneNumber']
            gateway = AfricasTalkingGateway(username, apiKey, "sandbox")
            try:
                regNo = request.session['regNo']
                fee_instance = StudentIdFee.objects.get(academic_year='2016/2017')
                id_fee = int(fee_instance.id_fee)
                amount = id_fee
                transactionId = gateway.initiateMobilePaymentCheckout(productName,
                                  phoneNumber,
                                  currencyCode,
                                  amount,
                                  metadata)
                print "The transactionId is " + transactionId
                return HttpResponse("payment initiated successfuly")

            except(KeyError, AfricasTalkingGatewayException) as e:

                print "Received error response: %s" % str(e)
    else:
        payment_form = PaymentForm()
    return render(request, 'payments/make_payment.html', {'payment_form': payment_form, })
