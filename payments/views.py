from django.shortcuts import render, HttpResponse
from payments.forms import PaymentForm
from django.contrib.auth.decorators import login_required
from payments.models import Payment, StudentIdFee
from student_ids.settings import apiKey, username, currencyCode, productName, metadata
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

@login_required(login_url='/login/')
def make_payment(request):
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            cd = payment_form.cleaned_data
            phoneNumber = cd['phoneNumber']
            gateway = AfricasTalkingGateway(username, apiKey, "sandbox")
            try:
                regNo = request.session['regNo']
                fee_instance = StudentIdFee.objects.get(academic_year='2016/2017')
                amount = int(fee_instance.id_fee)
                transaction_id = gateway.initiateMobilePaymentCheckout(productName,
                                                                       phoneNumber,
                                                                       currencyCode,
                                                                       amount,
                                                                       metadata)

                if transaction_id is not None:
                    payment = Payment.objects.create(
                        transaction_id=transaction_id,
                        phoneNumber=phoneNumber,
                        regNo=regNo,
                        status="PendingConfirmation",
                        amount=amount
                    )
                    payment.save()
                    message = "Request sent successfully please complete the payment by" \
                              "confirming the payment in you mobile phone."
                    return HttpResponse(message)

            except(KeyError, AfricasTalkingGatewayException) as e:

                print "Received error response: %s" % str(e)
    else:
        payment_form = PaymentForm()
    return render(request, 'payments/make_payment.html', {'payment_form': payment_form, })
