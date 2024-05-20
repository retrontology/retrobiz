from .models import Payment, Invoice, PAYMENT_CHOICES
from invoice.utils import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

DEFAULT_MAX=20

def index(request, page_number=1, max_items=DEFAULT_MAX):
    payments = Payment.objects.order_by("id")
    if request.GET.get("max"):
        max_items = request.GET.get("max")
    paginator = Paginator(payments, max_items)
    if request.GET.get("page"):
        page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "payment/index.html", context)

def create(request):
    invoices = Invoice.objects.order_by("number")
    for invoice in invoices:
        invoice.total = get_invoice_total(get_invoice_items(invoice))
    services = PAYMENT_CHOICES
    context = {
        "invoices": invoices,
        "services": services
    }
    return render(request, "payment/create.html", context)

def new(request):
    invoice = get_object_or_404(Invoice, pk=request.POST["invoice"])
    payment = Payment.objects.create(
        amount=float(request.POST["amount"]),
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