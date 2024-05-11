from .models import Client
from invoice.utils import *
from invoice.models import Invoice
from payment.models import Payment
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def index(request):
    clients = Client.objects.order_by("name")[:10]
    context = {"clients": clients}
    return render(request, "client/index.html", context)

def create(request):
    return render(request, "client/create.html")

def new(request):
    client = Client.objects.create(
        name=request.POST["name"],
        address_line1=request.POST["address_line1"],
        address_line2=request.POST["address_line2"],
        person_of_contact=request.POST["person_of_contact"],
        phone=request.POST["phone"],
        email=request.POST["email"],
    )
    return HttpResponseRedirect(reverse("client:view", args=(client.id,)))

def view(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    invoices = Invoice.objects.filter(client=client)
    billed = 0
    paid = 0
    for invoice in invoices:
        invoice.total = get_total(get_items(invoice))
        billed = billed + invoice.total
        invoice.payments = Payment.objects.filter(invoice=invoice)
        paid = paid + sum(payment.amount for payment in invoice.payments)
    
    owed = billed - paid
    context = {
        "client": client,
        "billed": billed,
        "paid": paid,
        "owed": owed,
        "invoices": invoices,
    }
    return render(request, "client/view.html", context)
