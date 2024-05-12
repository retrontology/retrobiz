from .models import Payment, Invoice, PAYMENT_CHOICES
from invoice.utils import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def index(request):
    payments = Payment.objects.order_by("id")[:10]
    context = {"payments": payments}
    return render(request, "payment/index.html", context)

def create(request):
    invoices = Invoice.objects.order_by("number")
    services = PAYMENT_CHOICES
    context = {
        "invoices": invoices,
        "services": services
    }
    return render(request, "payment/create.html", context)

def new(request):
    invoice = get_object_or_404(Invoice, pk=request.POST["invoice"])
    payment = Payment.objects.create(
        amount=request.POST["amount"],
        transaction_id=request.POST["transaction_id"],
        service=request.POST["service"],
        invoice=invoice,
    )
    return HttpResponseRedirect(reverse("payment:view", args=(payment.id,)))

def view(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    payment.invoice.total = get_invoice_total(get_invoice_items(payment.invoice))
    context = {"payment": payment}
    return render(request, "payment/view.html", context)